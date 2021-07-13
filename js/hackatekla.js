// ==UserScript==
// @name        hackatekla
// @namespace   hackatekla
// @description hackatekla
// @version      1.0
// @author       @zital
// @include      https://www.twitch.tv/*
// @include      https://*.twitch.tv/*
// @grant				 GM.xmlHttpRequest
// ==/UserScript==

(function ()
{
    console.log("hackatekla")
    let url_json = "http://localhost:8000/takatekla.json"
    let h_interval = 0

    GM.xmlHttpRequest(
    {
        method: "GET",
        url: url_json,
        headers:
        {
            referer: "https://www.twitch.tv",
            origin: "https://www.twitch.tv"
        },
        onload: function (response)
        {
            let j = JSON.parse(response.responseText)
            window.setTimeout(function ()
            {
                sendComments(j)
            }, 7 * 1000);
        },
        onerror: function (error)
        {
            console.error(error)
        }
    })

    function sendComments(hitzak)
    {
        let textarea = document.querySelector('textarea')
        let button = document.querySelector('button[data-a-target="chat-send-button"]')
        let i = 0

        h_interval = window.setInterval(function ()
        {
            if(typeof hitzak[i] !== 'undefined')
            {
                textarea.value = hitzak[i]
                i++
                button.click()
            }
            else
                window.clearInterval(h_interval)
        }, 2 * 1000)
    }
})()