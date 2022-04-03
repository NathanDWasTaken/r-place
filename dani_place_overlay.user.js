// ==UserScript==
// @name                r/place Dani Overlay
// @namespace           http://tampermonkey.net/
// @version             1
// @description         Shows an overlay over the r/place canvas, making it very easy to create and maintain our artwork
// @author              EvilTaco
// @match               https://hot-potato.reddit.com/embed*
// @icon                https://www.google.com/s2/favicons?sz=64&domain=reddit.com
// @updateURL           https://github.com/NathanDWasTaken/r-place/raw/main/dani_place_overlay.user.js
// @downloadURL         https://github.com/NathanDWasTaken/r-place/raw/main/dani_place_overlay.user.js
// @grant               none
// ==/UserScript==
if (window.top !== window.self) {
    window.addEventListener('load', () => {
            document.getElementsByTagName("mona-lisa-embed")[0].shadowRoot.children[0].getElementsByTagName("mona-lisa-canvas")[0].shadowRoot.children[0].appendChild(
        (function () {
            const i = document.createElement("img");
            i.src = "https://raw.githubusercontent.com/NathanDWasTaken/r-place/main/dani_place_overlay.png";
            i.style = "position: absolute;left: 0;top: 0;image-rendering: pixelated;width: 2000px;height: 1000px;";
            console.log(i);
            return i;
        })())

    }, false);

}