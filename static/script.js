const LOCK_DURATION = 10 * 60 * 1000;
let schema = {};

fetch("/schema")
    .then(res => res.json())
    .then(data => {
        schema = data;
        loadActions();
    });

function loadActions() {
    const select = document.getElementById("actionSelect");

    for (let action in schema) {
        let opt = document.createElement("option");
        opt.value = action;
        opt.text = action.toUpperCase();
        select.appendChild(opt);
    }

    select.onchange = renderForm;
    renderForm();
}

function renderForm() {
    const action = document.getElementById("actionSelect").value;
    const formArea = document.getElementById("formArea");
    const title = document.getElementById("title");

    formArea.innerHTML = "";
    title.innerText = action.toUpperCase();

    const fields = schema[action].fields;

    for (let key in fields) {
        let field = fields[key];

        // Create wrapper
        let wrapper = document.createElement("div");
        wrapper.className = "field";

        // Label
        let label = document.createElement("label");
        label.innerText = key;
        wrapper.appendChild(label);

        let inputElement;

        if (field.type === "select") {
            inputElement = document.createElement("select");

            field.options.forEach(optVal => {
                let opt = document.createElement("option");
                opt.value = optVal;
                opt.text = optVal;
                inputElement.appendChild(opt);
            });
        }

        if (field.type === "text" || field.type === "number") {
            inputElement = document.createElement("input");
            inputElement.type = field.type;
        }

        inputElement.id = key;

        wrapper.appendChild(inputElement);
        formArea.appendChild(wrapper);
    }
}

function runCommand() {
    const action = document.getElementById("actionSelect").value;
    const payload = { action: action };

    const fields = schema[action].fields;

    for (let key in fields) {
        payload[key] = document.getElementById(key).value;
    }

    document.getElementById("status").innerText = "Running...";
    document.getElementById("output").innerText = "";

    fetch("/run", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(payload)
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("status").innerText = "Done";
        document.getElementById("output").innerText =
            data.output || data.error;
    })
    .catch(() => {
        document.getElementById("status").innerText = "Error";
    });
}

function checkLock() {
    const lastUnlock = localStorage.getItem("unlockTime");

    if (!lastUnlock) {
        showLock();
        return;
    }

    const now = Date.now();
    if (now - parseInt(lastUnlock) > LOCK_DURATION) {
        showLock();
    }
}

function showLock() {
    document.getElementById("lockScreen").style.display = "flex";
    document.getElementsByClassName("main")[0].style.display = "none";
}

function hideLock() {
    document.getElementById("lockScreen").style.display = "none";
    document.getElementsByClassName("main")[0].style.display = "block";
}

async function verifyPassword() {
    const password = document.getElementById("passwordInput").value;

    try {
        const res = await fetch("/verify", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ password })
        });

        const data = await res.json();

        if (res.status === 200) {
            localStorage.setItem("unlockTime", Date.now());
            hideLock();
        } else {
            document.getElementById("lockError").innerText = "Wrong password";
        }

    } catch (err) {
        document.getElementById("lockError").innerText = "Server error";
    }
}

window.onload = function() {
    checkLock();
    setInterval(checkLock, 30000);
};