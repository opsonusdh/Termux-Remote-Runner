COMMAND_SCHEMA = {
"battery": {
    "command": ["termux-battery-status"],
    "fields": {}
},

"info": {
    "command": ["termux-info"],
    "fields": {}
},

"brightness": {
    "command": ["termux-brightness", "{value}"],
    "fields": {
        "value": {"type": "number"}
    }
},

"volume_set": {
    "command": ["termux-volume", "{stream}", "{level}"],
    "fields": {
        "stream": {"type": "select", "options": ["call", "system", "ring", "music", "alarm", "notification"]},
        "level": {"type": "number"}
    }
},
"volume_get": {
    "command": ["termux-volume"],
    "fields": {}
},
"torch": {
    "command": ["termux-torch", "{state}"],
    "fields": {
        "state": {"type": "select", "options": ["on", "off"]}
    }
},

"vibrate": {
    "command": ["termux-vibrate", "-d", "{duration}"],
    "fields": {
        "duration": {"type": "number"}
    }
},

"sensor": {
    "command": ["termux-sensor", "-a", "-n", "1"],
    "fields": {}
},

"location": {
    "command": ["termux-location"],
    "fields": {}
},

"fingerprint": {
    "command": ["termux-fingerprint"],
    "fields": {}
},
"sms_send": {
    "command": ["termux-sms-send", "-n", "{number}", "{message}"],
    "fields": {
        "number": {"type": "number"},
        "message": {"type": "text"}
    }
},

"sms_list": {
    "command": ["termux-sms-list"],
    "fields": {}
},

"call": {
    "command": ["termux-telephony-call", "{number}"],
    "fields": {
        "number": {"type": "number"}
    }
},

"call_log": {
    "command": ["termux-call-log"],
    "fields": {}
},
"download": {
    "command": ["termux-download", "{url}"],
    "fields": {
        "url": {"type": "text"}
    }
},

"open_file": {
    "command": ["termux-open", "{path}"],
    "fields": {
        "path": {"type": "text"}
    }
},

"open_url": {
    "command": ["termux-open-url", "{url}"],
    "fields": {
        "url": {"type": "text"}
    }
},

"clipboard_set": {
    "command": ["termux-clipboard-set", "{text}"],
    "fields": {
        "text": {"type": "text"}
    }
},

"clipboard_get": {
    "command": ["termux-clipboard-get"],
    "fields": {}
},
"camera_photo": {
    "command": ["termux-camera-photo", "{file}"],
    "fields": {
        "file": {"type": "text"}
    }
},

"camera_info": {
    "command": ["termux-camera-info"],
    "fields": {}
},

"microphone_record": {
    "command": ["termux-microphone-record", "-f", "{file}"],
    "fields": {
        "file": {"type": "text"}
    }
},

"media_play": {
    "command": ["termux-media-player", "play", "{file}"],
    "fields": {
        "file": {"type": "text"}
    }
},
"toast": {
    "command": ["termux-toast", "{text}"],
    "fields": {
        "text": {"type": "text"}
    }
},

"notification": {
    "command": ["termux-notification", "-t", "{heading}", "-c", "{content}"],
    "fields": {
        "heading": {"type": "text"},
        "content": {"type": "text"}
    }
},

"dialog": {
    "command": ["termux-dialog"],
    "fields": {}
},
"wifi_info": {
    "command": ["termux-wifi-connectioninfo"],
    "fields": {}
},

"wifi_scan": {
    "command": ["termux-wifi-scaninfo"],
    "fields": {}
},

"wifi_toggle": {
    "command": ["termux-wifi-enable", "{state}"],
    "fields": {
        "state": {"type": "select", "options": ["true", "false"]}
    }
},
"tts": {
    "command": ["termux-tts-speak", "{text}"],
    "fields": {
        "text": {"type": "text"}
    }
},

"speech_to_text": {
    "command": ["termux-speech-to-text"],
    "fields": {}
},

"audio_info": {
    "command": ["termux-audio-info"],
    "fields": {}
},
"wake_lock": {
    "command": ["termux-wake-lock"],
    "fields": {}
},

"wake_unlock": {
    "command": ["termux-wake-unlock"],
    "fields": {}
},

"reload_settings": {
    "command": ["termux-reload-settings"],
    "fields": {}
},

"setup_storage": {
    "command": ["termux-setup-storage"],
    "fields": {}
},
}
