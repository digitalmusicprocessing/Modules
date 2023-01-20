---
layout: module
permalink: /Module2/Video3
title: "CS 372 Module 2: Simple Numpy Tunes Part 3"
excerpt: "CS 372 Module 2: Simple Numpy Tunes Part 3"

info:
  prev: "./Exercise2"
  next: "./Exercise3"
  comments: "true"
---

<p>
Please watch the video below, and click the <code>Next</code> button to continue when you're finished
</p>

<iframe width="560" height="315" src="https://www.youtube.com/embed/WBBm7E_tcUU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<head><meta charset="utf-8" />

<title>Part3</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Making-Tunes-with-Numpy-Slice-Assignment">Making Tunes with Numpy Slice Assignment<a class="anchor-link" href="#Making-Tunes-with-Numpy-Slice-Assignment">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">IPython.display</span> <span class="k">as</span> <span class="nn">ipd</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>$ f = 440*2^{p/12} $</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">get_note_freq</span><span class="p">(</span><span class="n">p</span><span class="p">):</span>
    <span class="k">return</span> <span class="mi">440</span><span class="o">*</span><span class="mi">2</span><span class="o">**</span><span class="p">(</span><span class="n">p</span><span class="o">/</span><span class="mi">12</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sr</span> <span class="o">=</span> <span class="mi">44100</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">sr</span><span class="o">*</span><span class="mf">1.5</span><span class="p">))</span>
<span class="n">t</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">sr</span><span class="p">)</span><span class="o">/</span><span class="mi">2</span><span class="p">)</span><span class="o">/</span><span class="n">sr</span>
<span class="n">off</span> <span class="o">=</span> <span class="mi">4</span>
<span class="n">y</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="nb">int</span><span class="p">(</span><span class="n">sr</span><span class="o">/</span><span class="mi">2</span><span class="p">)]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">get_note_freq</span><span class="p">(</span><span class="n">off</span><span class="p">)</span><span class="o">*</span><span class="n">t</span><span class="p">)</span>
<span class="n">y</span><span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">sr</span><span class="o">/</span><span class="mi">2</span><span class="p">):</span><span class="n">sr</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">get_note_freq</span><span class="p">(</span><span class="n">off</span><span class="o">+</span><span class="mi">4</span><span class="p">)</span><span class="o">*</span><span class="n">t</span><span class="p">)</span>
<span class="n">y</span><span class="p">[</span><span class="n">sr</span><span class="p">::]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">get_note_freq</span><span class="p">(</span><span class="n">off</span><span class="o">+</span><span class="mi">7</span><span class="p">)</span><span class="o">*</span><span class="n">t</span><span class="p">)</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">y</span> <span class="o">+</span> <span class="mf">0.01</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="n">y</span><span class="o">.</span><span class="n">size</span><span class="p">)</span>
<span class="n">ipd</span><span class="o">.</span><span class="n">Audio</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">rate</span><span class="o">=</span><span class="n">sr</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[5]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">

                <audio  controls="controls" >
                    <source src="data:audio/wav;base64,UklGRvAEAgBXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YcwEAgCOe+R8sHmgeFB1vHGMbAFp32P6W2tXOlDcRwJBNTcfLx8kmhx2E64IAgDD9U3qeOFl2I7OesN3vE60JrCTqL2gpZzFlK+RV46miLCIzIVJhE+EkIP5h6mIDYrKjt6Qbpmenfek9aolsHe4NMRkypTUfdlR5Trv1/mCAp0OvxfuH9QpgTL0O59BDEuEVcxZ3GB/ZIBr3nKhdfJ0QHq3fZh7l3xxeSN6BneodPxuhGrSZ/pg/lj4UmFNaUT0POQy6ydMI6YYPw6NBRb7fvEA6S7dLtLGyxbCT7lmskqrkaWKnTSYNJX3jheMZoigh6yE44N7hR2Ezod9i7CMFJEZlu2YAJ99pkGuebaCvqzGvM/51p7hE+qG9M7+xgdLElUeXSRXLhI3Fz4QRnhOnFW8XLtjuGYobHpwxndud197/3rsehV6oXtGeRd3rHNQbvtqHmXkXedVIVGOS61BOTrqL7clxhkjEnQJ7v5M9ofs4+HZ2PrPDcg0v0K3u68PpiGhkZxsloePVI6IibqHPIZvhYSDhYQbhSGEFIe9jb2S4JjZn+6isqnQsHy3TsB9yYPSsN7D5gbvefcgAqsLsxW4HbMqOzGXOLBCEEtrUbZZvl1EZ3Brlm0FctZ1yHkperh6qH2yeSx7B3ZCdzpxkGs5ZqxhQFu7UaRN6EQZPUozzyv3IT0YihB+BUf7q/B26Fbe7NUjzTvFDbnOs5yrH6UPnZ2YDpQDkL+M5Ic0hAmC/oMGhrmEHojgigqLxo4skz2aeZyzpE6upbTbvBfHYsym2Abix+sl88f8UgfZEMwa0SLYLVo2eT4XRW5Ol1QWXAhj4GokbspulXfHeAh6aXwMeUh59npSd2R2vHPebRpq7GNJX8NYnFAGSO9AZjqJL0wnBh6dFSoLTQE4+dntOuTf2mPRC8k8wlq53rGyq12f85pGlAuSYY40i26HQodSgReCUoRmhkqHmovhjA2SZpaymzWi7arFsKa3OcC8xoDSh9oX5PvuePelA+YKpRUHITgptTBjOdE/BkuMUVtXS2FtY51ps21qc7B2F3kCeTt5JXrpe1N62nSvd9VvkWxJacliOF18VgdN10PIPXI0wizUI+QZ8BBoBe/6K/I56tLexdepzDvF4bzks4urM6WNocCYMJRpk4uKiIdKhxCFoINChRmEE4eKiG2J/JBqlXSWAJwYpeKso7JfvI3Fxs0J1dneQur170X9wwTJDQsaBCO6KU82ZjssRRhPflUQXW9hqWbfbM9xL3VmeCR59nqye/J5KnoYestyW3E+cMdrqGYTYVxaQVF9SVxDlzjrNE4nLx9cF5YJPQI3+GzrfeVO2l7RO8hLvvi6A7ByqUem050RmY+Sgo37idKJX4UCg0WDfYSRhPqHbYktjLuQmZbQnM+hUajFr1K3nL6NxybRftvp4sLt+PZ0AAQLoxV8Hi8mJTEfOShBMEc6T+tXbV51ZchrlG3QcfpzzHmxe4F6BHkhe5l5tnj7dkZzk2/3aSNh9FoEVRpQ20dcP/83Py5MJKobYBJ1Byr8aPKH6Xng1NdQzqzFFL2NtqesMadknbubZZTNj+yMiImghRmE2oRahC+F1oeBiqyLJpB0lSqYuJrvpO+qcbQVu0HEFs1e1RneIuXM8KP7/wPnDUUYZCLPK5gzzzubQr9MF1SaWShi2mcRbMFuQ3R8dn56nnqhe79953r0eAV4dnLKcAFt1WWmYXJYVFRgSbVECDwFM/4pHSG2FVQKnwIo+dnuDOY53UDSgsn8v9i35rHCqQeiOp2YmYSRBZCKidmIzoUFhVOEFYZThveGuInfjbCPzZQDm92h1KjWrlq0Zb/bxUnPI9gd4R/qJPRK/qEKERIMG3Il/jDqNwRASUkwUS1YGl4PZZ5pLWwhcx51FHr2erV7/XrIe915RXhrcmhyDW0KadhjlF0KWK9Q5UWAQLA3giyjJGQb5RCMB5T9dPVn6iHiptULzvrGwL4KuE+vaKWEn/qZlpZ5jwmNNYndheWE9oM7hF6FloemiSiM5o4/kQOX1Z7Co6+rfLG4uULA4cdj0yHc2eUH79D5fQXbDiEWbSBTKUUy3TvORN5KhFQRW8pgTmYbbeBvX3MjdzJ6vnude6d9Bnwiedh1N3Wkbptth2Z/YqtbuFMtS5BC3zkFMlEpBiELGKwNkgM8+OrwjOeT3efTncwkwpW59LDmqsajh56pmK2SM5BVipOIRYTDg9mDFYQ7g06Id4mvjQuQG5UumnKfjqgbrV213r6SxYvPUNib4ZPq2vRF/NMIIBRbHKokUi6aN8FCpkaLTrpZ71v6ZO1ntG7Ycv53HnhcekV6aH2Aeyd6jnnndLxyx213ax5l3F7wVSRQv0mIPE428C1sJYUcJBHvCB3+cvQ87OniM9iFzo3G3b07ttmvmqdRoEmbzpWNkYaMDoj7icaGw4SrhduE1oWaiwSKvJDPkeuVOJ7Po7WrW7GCumHAnstZ0NjcZuaX7yP3fwKNDpUWmCCDKLIwkTs3RHFJJ1QYWbhfMGbKbe5xKXPodDN5NHqlfhF8znn9eo12fXO7cgxrt2csYIRcQlR0S1xHFj0wNbkoeSE7GfgMygTD+l7yJOfR3PLUIMwdw4S6XbJPq7+kOp0Zm9WRtY6EjDeIqIVAggWGcYM8hqWIpIiJjFWPDJQDmV+fJalSrTa0j72lxo3Ls9es3XvpVPPI/YoESxCyGssiFSygNwc/CER2UIRYr1xLY5loeW2FcAF0Q3cIemJ6IH2xe4Z3jHeddSRxCG2AaAtnNV4LWOxSd0gsQ2Y38DAFJgIcPBScC8UAzvZl7qnlP9r8zzzIrL1JuJewGKj3n82c8JYukYmMAou4hXiESYSHgr2DWIUhiJ6IwIyqkiCWR5troQWqg7D1t/nAa8rHzz3dCeUV7/z2iAJuCxwUhh5UJjIyhDvjQpBJ/1EVW91fz2cka8FuT3TGdmx5SHqsfOx6CHwIeDt3w3MAb01r6GbYYZVbG1c4TFlHoD60M74sAiE7GcoOEQaw+s/xPOn43zLWfs1kxV67U7OWqwKlAZ/+mNyTiZF/jJKHjIRhh0+FeoJ8hVOHP4o9igCPlpUomlage6YerXmyTryJxnTM9teG3vXpB/N5/0sGgRFDGT8iAS2TNaY9e0c8TpVUvlovYStmo2w6cepybnZteit8i32beph6OHnZdYxz6m/zaQRlJ2DWWcdP90uQRGE6HjDmKZEe/RMnDPsCpvj+7MfjFN7VzxDIB8Cvt2+yZafrolacTJamk4yLZosJiFiEDoXig9CFjYYbhz2JUI5pklOUjp1zoYOpq7Bwt62+dslL0fPa2eNZ7HX3IAJPCeoSCR5OJ6wuLziVQfxJrFCGV61c0GWBawlwHHKMdIh5+HocfKV8lXvUef93xnNFch5t4GehYatc3FWOTRtGiz53NjstaSRXG1gQwwaR+znzq+lh3UvXe87nxSy8t7O7rcimZ6FHmX+VLo7Hi22JMYjng8aE2IG3hGqIWIi/jHOOQJQolwqdBKWFrDGy7LrGwgTNHNPz3ejlXvMZ+k4DERBmGAki0ysXNJE89UOOTnlU81uHYUxm+Wp+cptyGXZEdwx89Hkqe1p4oncadzVxcnCbbQ9mn2HMVzJTsEkCRfs5qzBSKNMgShR1C0sDDfaw7ZPl2twr0sHISsAjtjmwD6n7oZ+fs5bLktqNb4g7hxOESIYXhA6Haof5iG+IiIvPkb2WMZ0yoCKp2LE0tb+9SshszoLYKuHb6zL3zwCECx8SxhykJVgvvzcJQJhHRE8eWCleTGSJat9sG3KSdWx53Xm9eu16qnrMdvV3AXfmb8lq5WiwYpteblXOUF1JXkDoN7MrWibeGqERFQdu/aX0uOjN3mLYm87iw1e8Y7Ueq3mk3qAanR2WWJAWjLqJx4bThCWF0oSxhOeGGoj8iiiO7pX3lrWfuaTZq1Swsrlew/3JH9QQ31rnhfG0+h8EcA7CGQwf7SlQM3Y7rkQWTYRUuFrDYMFnOGyCcEN1U3Z+eUh75XuKewh8MnlUdSx0Hm6QbYtpAWCCWctTPUuaRP85qDF/KKsfWxVMD5gBEfsJ77HnDt7g1drML8GruvqvhKsBpNecLZdXlLmPt4ksiJWGyoUghGCFsISDiGmJNY7akvCVkpqJolSnxa3itdW9XsaKzrDX3eNq50P1WP0bCesTORvJJpEvSjelQGNHmFIbVqVbnGXManptR3Svdth3cHomfKZ7kns0e29463ipcWZt5WilZftcT1gyTvpIqz/1NWcvfib4G10Uqwiu/k/1GexP4EvZKc9kxe68VLZTrC+n6aDKmQeVTpBWjZ2JiIdNhKiFgIJlhtSEAompiuKMOpUFmOebVqRZqqmxyLcYwrvItNZU3dXok/Dn+VIBIA01Fs0g+yrXM6s6PUU6TDNUEFkpX6xluWpbb050QnU6egx8WHt3exB51nl8dOJz7XBTa6tmHGKjXBZSw03sQ0o71TL1KoIeGBjCDAEEc/sI8mXlwd6E1uTM+8SJu0WzCaxBpCue05k4k4GOLor/iDWHkYP5gg2FPYXChtiKSo2HkPKT4JmyoLmmGq3utSe/AsYIzprWOuB76R/0jf2HB6ISGhn7J/MuqTWaQBRGoU5DV0ddJ2IZaftvinIldcl5TntefLN6oHkee2x573SrchZuzWr2ZJ1dUVofUj1IK0B9OOAu4iXCHkQU0QoVANnzDez54P/b5s/Jx4fAC7PYrx6pQqCPnBaWc49VjYaJ9Ibzhf2D2YMdhFmHmIeOid+OPJIyliecy6PaqpKxP7lywaDK9c9h3FnjMu0g9iUBfQooFEIf9SeGMgg8oUGJTEhR6lafXqxlvGs0cCRzHHrPefl50Xvjen56Q3nQdZV0TnDWaU5m5GILXD9Utk1FRfI96TToK0Mj2hehD8QES/vi8dDoJ92502/LUMKBuuqziasupp6dcZn3k26PZI3aii6IH4Xzgm2F9YQQhu2J/osekiGWCZiaoCml4q0KtbS7ncXYy7nVyOA86Iny5ftbBjESARv0IkgrfjQPPcNErE1ZVpFdaGQYZyFs0nLndId3L3peetJ7qXs9eYV4QHllcyNvUWqxZXJd3lh7UvBKnkFOOWUwXicmHD0TAgue/2z4/+vN4xTbYM8wx22/Lrl9sSyo+6EEnGKV0pJgjZuJ8IaThQCEf4J2hNKFcodKjPWN15CLlvacdaMkrLSxK7hhvvnKOs+020rjv+0C96UAOQu5FmUf6idoL4w6XEA1SntQHlgbX2JmeGqucddx4HYQd155rXxAe8Z4oHtWdqV1jHHgalJlu2EjXUdXnU41R1k+pDXaK0wkChuREA0GzvyD9CTsrOCq12DNOcXOvG+xvqqKppOh3ZmNlJWOaowKiGiFH4YKhJaFsYbBhuSFKYyrjhCTVpronvGkn6wwsSW7dcNOzBnWTt+96cDyW/0fBvwPQBgZJN8sDTYaPINHc06KVWFbmGK1ZylsHHAddC13uHame1d7jHmIeRd6jncudLJwnmvGZsdgoFomUsFLy0IIO1sxKyaCH/gSbglX/0f4Yu0x5fbb+tAHyGjBDrp6sESo+aC5nOyVdJKsjpmLnIZ+hwqHRoW8grGEgIdKiXqNnpEik/Cbl6BOp3yyAbi4vzvIPNHA2O7kDuvp9RsBTQouFaIdkSYwLhY4hkLNSApRj1lfXZlmr2kjbbxy1HbBesZ573lneid6G3nrdhh0fHDQbUporWEOXvtTxE9pSCRAbTYJLn0j6BmhErUHofwV9CTrh9+P1QXMv8Nhuxi1DqyjphSgOZqulBiO5ok7ipiHyIRhhECDf4Vph2SIp4y8jg6XsJl1nUGkDKz3su+66sAUy5/VDN4O527w/ftSBd8MNxhgIu8qFjSsP35EqU0nVoxcgGG9ZcZsum5BdJx5zntEeTt8SnvXebp5xXYPc2pujGsiZpthp1nqUFRN1EOtOyAyOCmKILEV2gpyAOz5fe5B58DbM9JSy5DBabrQsFaqPqNHm+KUs5O5kNiLyIhHh9CFaoZfhuCEpobkiFCN5Y8olkCZwKDHp6mtFrfwvVrHrs/O2N/hx+3U9XwAZglzFKsbsCYXMBI3h0DZR1FObVbMXTJjv2bAbw50r3Znd895iHmeenh7SnkoeQ51t3GubYFpe2OAW/NYu0/cR/8/vDVuL4MjvRzuEHIJwQDa9u3rJ+Ef1rvQAcbnvnG0XLAdpeaeKpullSGRZI1Vih+FNIcqhSqGuYPHhOmICYtGjQiQkZngnXyhqaq5sai6UcKRyM7Tvt385ebsUPmoAtENUhf7HxgpWjTQO/VCb0rkUy1aSGBwaEBr1W7IdO93W3lRfCh7Gnslewt4OHh2czZwBm3mYxhh9lteVldO9kNxPGszXypZIcwWnw3FAxr5uPL45q/cZtNuy+G/W7g0sSer46Q/nBGaLJMojx6IG4m9hBeEK4SrghWEqYWSiRmLC4+pkyycbp4npUWvCbbWveHH9M1/1xvfkOrn9LD+uwjTEQEcOiaPMQc3Xz8TRoJQ9VVTX5VkVWhvbz1yRXVAeFx7+3n8fAl6d3oseDd1W3OObt1p6mPuXsdWp1DrRQNBIjdKMZsk3hsyFIUI+P3m9HDsU+PF2qHQGsibvcy3DrClqD6hwJyclhKTKY01i6KJ0oTnheSCpoC/hdKL1YoLjleTepehnOel3Km/sMy23r9wyW/R5tw95LHwcPcaBAwLzRU/H3QoMTDuOZRCukuaUrVZRl9JZMNqkXFvcnh2n3b7e9p4DHyYfQJ4/Xb3dGJv6Gs/ZKFgE1v+UnhMGkOvPMkxTCrZIIoZDBCzBHb5bfFr58ffStZkzBzEJr60r2+rYKWUnWGZLpKtjtOK/4aLhouEYYMjhJKFw4kkiTyLV5JllrWYx542pkqssbQlvmDG5c7f10vhLetq8dX+gAh1D68ZpyTiLKQzAz3oRHtOFlbsW7FhyWdIbgFyHXSUeM955Hu8emh7rXiXeNN0OnMdbu9qmWU1YCJYflGDSehBUDihMK8lDR5xE+gLvAEb9mXrsOTp2k/RfcjXv6+3urDOqYSiUJxYlXiQH47fiECHV4U0hB+Dw4TbhYeGVIs6jFOTl5drnFKjHapJsWa3gMELx5XTZNmH5STvO/dTA+IKXhXhH/clszDkOrhCFEgjU0FYlmACZGxsGG7TcL92/nlTeFB7h3pPemJ52naycolwbW3dZ6NkEF7VVKZNgUQfO8Az+Sv9IE4a3A4sBgD7FvJO6s3cN9RqzVLFarz2tGyu7qdBni2b1ZXHj+aLX4hohjWGA4TohYGFsoSshWyNRo6Hk1ya95/jpYStQrIPvDHD281h107feOgY8on8/QPxEPcYJiJULNM0mD+fRzdPvFInXM1h2GaNa6txPnSAeKp4hHrUe9966Hz/eBF38nNucPxrlWRgYAJZiFCxSW9CEDo/MRsokB1LFWcKygId9wjtJ+NB2yzTN8lpwOy3JrL+qZmhEJ3ClK2RYo6ZikuI0YYlhbqCAoKBhHyIJYp6jiuR8JVrmyygFafzrkG3uMBWxw3Sk9oX5Nbte/Vi/4sI8xS1HxMo+TGqOVFCEUmSTmhYKV82ZhhqqW46dKF2dXb4eTl7BHu/eg14IHh0dQdxK2xEaOpiNFzlUsVOtUdcPqg01ixCI6sayhOHB138nPRx6frg8daizSXEf76dswCti6WenpGai5UWjm6MTokohz6GjYR0hUaDg4bgh++JMo57kyiZN5x1pEes7bKnu9jCd82i1Zfe3ueV8ZL+GwQzDxAXhiLGKrs19zoFRe1L3lN3XtNgSmjpbdhwTnbIeHx45HrvfGp9gXrOexF4WnS9b5Fq+GU1X/paw1KhSwlDMDkVMX0n3B+TFNYMSAC++ObtYOfl3LPR2sqRwiK6FLMtqqWjupw0l2qUv43ciZ+GAoWzh7iDToeRha+FroqLjMKRU5ZempKh7aTqrVi2cr50x/jQm9ls3+Lr//Ox/V0JDhS6HRAnCjGcOGJAcEYoUeRXTV0YZJZpXm6pc/9yTHoZerR7rHv4eqF6QXmddTxxpm9ebABi41uoVahPykjjPbc32iwUIyUbrBFkCU77AfWL6hDjvtgP0b3GU7xEtsCscKRPoEqaSJiwkO+MLYppiSeGKYKTg9ODYYf3hueLaY8Dkl6bMp9gpM6pX7O/urLD1Mrm08fc7OU58Gz63wLYD4QWFCHALj8x9TzqQo9OJlOOWydgaGefa65xRnFHdgp6gHtVe2t5U32xeAJ3kXIxbvBqX2YrYHZd1VSNTXFFtDumMcYpBR9IFogLSAKc91bvUuaO3KHQXc1uwba7RrIPqRKmN51Sl4GUVY38iomJrYY8hsCCpYZfh02GIokPjX2SCpTGm9aguKT7rT21M71WxcvO0tc65HLooPTR/LsGihGzGwYn4i1SOJo/zUcZUV1XaFrmY2ZnbmxQcdZ4w3hFeu15+3nmer95wnd9c4Fzb2yxarRk51wRV2lSXkfuPbU3SC0lJSkgOhIkCYH9fvVc7HziRNdV0D/I17uXtWyvX6mBopyaIZUWkv+LIok/hteH/YUig7SCnYXph9yL644eki+ZRKArphaq+7Pat/3C+Mrt05TciudU8FL7ZAQCD+EZpSFHKoozhTyUQ21K3FEmWdReUWVla5tvzXLLdKN5wHurev97R3t9eFl2m3RxcFBr7GkdY3dZv1IdTMhFbj6+NDwstCESGSYOUAN/+STxpOhQ3SjW4c3Nw5m6ZbEjqqukaJ7emUSR6o3bijWJGodBg86FwoRKghGHRYlqjdmQrJRkmSKgT6cwrwm2k76ExD7ORddT32zrbfQa/1cJvBDfGgEjbC1CNXQ/I0lZTjlVsFqoZSloAm6gb/hzmXifeFl7RnxtfV95LXgjeAVzO28ia6diOl0fWINSx0j1QOo4iC7UJiQclBLnCKX/OPcm7AjiHNyT0GHGCr/9s5WtQah4oXGbr5QFk/WNH4x9hgOGLIX0g9KFP4eDhg+MPY7ekTiW+J3NoviqoLC6udHAPMgP0lzbv+Wi7Yr5WgIaCysVhR7HJwYwljn8Q69MrVLfWOFfmmQha+JvPnGldgp5Rno+e9B80HnAeER2mHb2bmRrBmcYYSlbvlNXTTpFBz3cM3YqaR+HGosPwQQ7/OXyDurJ3hbV68z6wc27BbRRqqKkp56RmGqT941zjxSJpYb/hACDOITrhDmG3ovAjfyNTJRzmmefj6WHq2mzs7ztxaLLA9bJ4LDnZ/Iv/f0FiRHlGckjtSzqNGU97EagT0ZXj13dY+xnzmsKccJz0HWJevt9H3zDesx3AXtNdsh1fm0ybE9mAWA5WHRRbU2PQog4ey4jJ0AeJxXmB13/n/Y47PfkONoh0Z/LaL7bt/KvXacBogmbN5ZJkZyLAov3iXKGhoISg+6DhoanhkmLdY54kM+Tw5ouohCqpbA3uWG/UshszlXbfOMh7uP5LwIuC8kVhx7RJo8wxTjIQpJJN1CoV7JggmTqak9uZnKOdIV66Himemp8jHo3egZ4/nUlcZhtTGiyYkBczFVdTsFGsz6XNQkrwCOuG3sPlgYm/yDyI+nT3gnX7syUxFi7qLFvq+qmY5/OmSeVXY9gjVOJzIZ9g9uDe4N/g8qEfIvNitKPbJINmX+gKKb/rZexI7y6xKXJ/9Yz4GbnSvIA+4YHRBC5FyohNi24NGw9hEaVTg5UOVt9YrxnJXBkchd17HiNd7h9yHoLewR84XlneEFzp2/UZxllBGEhW1VSAUsCQZo6QzErKLsdvhesC5sDS/ui7Rjmht0ez5bIPsG3tlSx5anjoNGeL5cFks+OJokCiKiHn4Wcgv+D+YSGh16KLI6Tk6KYeJsyol6nzrDXt8K9asl20ffbYuLq6x72bAFkDDcV6RuZJj4wcTn/PwBJz1CIVxZcDGZ0aPNw6XEFduh5r3zDe459f32Ed59203QDct9u5WnjY71erVdaToBK1D5dOS8tEyRcGqcPWAcc/UHyhOls4JPYR843x1G79bQwrfumpZ8ZnACVfZCriwiKRoijhfaFaYFBhDaHK4kFjGSN6JKWmDud86GCrFyzHLs1v3nKXtJV3jroRvGm+UYEcQ+7FUsh4SmvM1g/MkZqSGtTNFmtYM1nr2zlb+xxsHkZep57dXureip603oKdll0SG6qao5lRF9lWZtThkp/RcQ6yTIhKoIgMheZDK4Bxfpo7nDn1dq31ETKiML2to+wHKobo92eTZaUkg6MHIu9hmWJTojtgraEuoXKiJ2JnI29kcKVb5pRokCqda/KtlG+3sQ1zkbVr+Lt7mj1D/8CCb8Rhx2qJ8At0zf9QG5Jq0+GVTBdo2SvaFdtdHKVdiF4EXwVffd50XxGeRd4VXcTc4Bs6WmdYtpcLlfxTxxLuEC4N3owpCWSG1IRMgmyAG/2C+v44qTYks9byOW9ULVyrd+n1J9EnLyV3o3PizyJp4YGhpCFlYWVhBGBDIfDjFuOIZL8lu+c7KTNqWWxI7wqw43L/9IQ3oTmq/Gc990D/gxBF30f/yf7Mvo6pkR6THdTn1kqYkpnFGukbq1yCHY5efJ6rn1Ve695QHhPd5lyhXDea7pmoGPUWWtUekyuRf86fDLKKwAi4xhQDWEEj/l270Hmd91O1FTL8MJFu5KywKp/pd2duJhXlC6O94p+hnyIYIWjheSCgYPvhRSKpIqjkq+VOJmXoMWmRq74tUK+dsYBzdXWbuFU6XDxqP38BkQSXxrhJlEucjZPQDZJylDTVYdeTWPnZ/Nv328Fdvp64nifeuZ8C3lJfCF2w3TIcvBuo2ktY49eoFcHU5tIVkIlONgugSYzHP0Rogj7/432BOyI4rHZG9HhxWu+97TPrQ6od6FLnySXepFijraKAYf9hJWGXIMAhf2DrIgfi6eMdJOPl/2c/KXbqlKxwrhdwTfMotN73YrkB+44+RoBNgw6FogfnSiWMsE6tEM+TGhR/VnEYM5n2mt3b/xwrXVIe8l4I3yRe3F7WXqJeEpz6m58bKtlC1/uXWxVb046RhQ9ZjOvKsQibhd4D/AFc/xZ8nDpEt60023M+sNnuyezGq3epFCfCZe1k7mQOI3lh9WFs4NihDaE3oVXh3uHv454kmyT/Zrmn4Omhq38s0u9i8PFzT7WquHP64ryS/1oBl0QXxlLI78sJDRkPV1HR04IUyhdgmN8Z+Fr6XOldP54vnikeqZ73Xlce+5553ORctxuWmqEZTZfj1l8Uj5KqUH5ObkvNijHG4sVaQrW/zf3be0I5XbYtM9ZyUjBHbc6sDGrAqHAmuKVQZEij+2J1IaLhMWEhYKsg2SGuYeUi56QFpSeltyam6IdqciwA7jPv9HI49Ei29fk/e4a+NUA8QqSFLcf3CggMIg3qUEbS6BRtVm0X61lKmzebtVxE3eVefV633wIfFF8b3ryd7p1fXCRbX1ox2S3XIhUNk7+RgI+ZDXQK34iSRjMD9EEDPxi9OPnDd+O1+bLXcNOuii1aawhpkCf1JfylbuNoopQiLSG7YXvhDGFgIbNh+CIUYvgjmiUwZjWnm+mb611szK80sNqzf3VTOD95mH09vz+BNcP5xq5IuotVjW+PtxGdk7GUgVd6GG9ZvBuL3G+dal2hnzxeuh8hXvveQN6hHUgdBdwdGoKZlJggFgAUldKxEPfOy8w6SU/HocTYgsmAMf3ie2X5gDcD9JXybrDWrlIsOmqR6O6nEiWv5CCj/mJ7YZdhe2DeITShd6Fy4i2imeO+JHylyKcMaGhqGquzLemwOrIXtCm2LXkyu9P9sABMQsHFGAdQyhrMMY4qkGuSf1QzViVXZ5otmgTbUNzx3YHef97Fn1jey98B3lReIB0sHLdayNnPGQsXBBXQU47Q3g+jjWULBAkqBoJEDUHQPzo89LqSt7p1kbOaMQSvFy1t60rpdGeypenlMOQf46aiReERYKig82E8oPsh72HRYvlj6aTuJabnBikcay9sWG6cMOOzd7SSN2f6LLyk/rGBucN2BXeIQEqITP+PlZGMUouUttbI2G7ZBxq6294cnh4OHrVeuh8NHpseHJ5B3kQchJv6mmjZcJgg1rLUXlMkkNuOgIzVimhHz0VmQoOAVf6hPDM4qncLtH1yVbAx7lzsMeo96Lim1SYC5PVjQmIOocchz6HoIOhgzKFRYj/iXCM0pFolq2ZxZ+WqBmu2LcyvgLHq86L2G3hE+wT90L/twjJEXAcjiLcL4s6AkL5RstPOVc8Xj1m1Gr2bWJxu3eSeJR6ynxWe116K30aeHN2pnTebPdor2VJXn5W500VSCs/ADiKL2wl6Bs8EhwIIv1K9kXsg+GB1zvNYsb1vNi0ia1Bphqg65uDlG6SMo1uibiGmoTGhLeCSIVGiH6IbY2djTySypZam/2heqkQtMu71sLPyv3TQt0b6CDw2PvvBFAMEBkZIPEoODIqOnVEDE5OVFJYq17SZS1rm269daR3kntGfNp6snpbexh7rXX3cypzlGsuZxRiMlhRUdRK90SiO4Ix2iq0HxkWIw2xBNf3DvH+5DPeStF8yybCO7klsJmpkqNWnfGU1pPTji6Mx4jnhfqCEIUyhBiGKYjBiTeLV5B2lj2ZJ6FrprGt2rcpvNzEoNAy2Z7hSesY9cj98QgWE0cd8Sa6LhU3jj9DSd5Q8VV+XOVli2eXb51xLHMZeGN5XnobfFt7tngBeTh2sHICcJpqmGUVXiBYg0/FR+I+4DbZLL8mtR2RFHwJ4f8q83TrruML2o7Q68ZWvxi1ha9bp/yfD50SlcuSm4xbiF+H3oUPhASEzYXZhfmGtow5jDGSfZkondilAqrCszG3D8FkyUvTst5t5vfuPPjUA6UOfxiwIHQowDOjO3FFtUrCU8JaoWFkZYlpW3DPcu513HinfO19jXsifKt4k3elc4xukG5baBthQ1kBVa1Nx0V9PSIyXylDIvQVSQ5QBBj8cPIh53PdWdYUy5nDRbpMsRCrBKRXnt6YxZREjtqJ5YlTh5GF/YJhg7CFEoeji2CMiZFRlA+ah6Avp+2slLVsu83EDczb2ErgSu169C/+PgY1EhQa+SQgLNc1bj4wRvRNFlZDXPNiZmrybbdxuHRddzt6vH2TeLx6DH1ld950enXxbrZn2WWEXR1ZhFDZSNM/RDeiLsUm9xq/E7IJDf+09YHr/uTT2PzQ2cjpvQO3o64dpxmiJ5sKl1uSUY5siMqGlYZYhJ+G1IUCh9WFW4txjjqTxZcdnXijoakgsFa4OMAhydHUFtxY47ftN/nkAhQMhxW3H20oLDIMOaFDt0iLUGpYXmCvZY5p/m/DcpV2xHjbfA98+HrkeuV6YnZkdJduAWxZZ1Ji5VqBVYlNGkXCPkM1QCzzIVMaKxAgBzr78++N6QjestTKzEjEIrwns7esZqQiniaYmZR1kAGPnod4hLGFnoTChKqHuoSDhhqNSJCLlpSZYZ56p66rCbRzu2rEkM5t1pbfD+m38sz7lAg/EPMaDyONLCg0lzuZRQJOj1R+XChmUWm/bN5zgHWId5t6tXowfFh51XqjeSx323PWbNBnB2UPX5hauE8MSbFEPjkrL6snBx/tE7YLg/+A+IXvH+RB2vTSVch9wsK6/67Qqf2hzJ3DmEWQFo9tjXWH2YULhVOECYL/hgqIj4uQjrCTlJfbm2WkFqc0sc+5Ib+CxzLRRtn54knsVvapANgJyRQ4H70lXDHmOeVCwE1sUx1Yc15FZuRr6m5hc+J3ZnhKegd8QHl2e0943HgzdkFzTG7GaC5gZVwXVrNNsUcEPts00yv4JGUZshCVBbH8dPUa6Ifft9Yty1PE5LoNtE6sVKbVn3acO5VGkC+NeYsfhm6FVIMvhLGFvodsirWLTJEHlNiZA54zpnSrQrR3ut7CTs0z1j3fSOtL8gT89wRhD4IZ8yCPLI0zrj7SRntN61QlWf1gd2bobLJy5HSzd8N5EXwWe9V6MXo0eMt22XLKbqZp2GRLXqhXgFH9Sr9C/zhxMXYoiR6uFc4KGQHz+tLuDecN24nPIMvSv9m3ja6eqoykm5oulluT0Y4njK+ID4VkhZqDAoUPhDiGRoibjO+ONpfOmcmfQ6mtr2W40r87yPHSXtnf4mXrM/USASUKRxJvHOEmHzBtOTI+vkgoUflXZmB0Y4ho92wjdKd2CHojevp46HlVexZ6qXruccRxd250aAdk314TVpFN10b2Pzw2OS1hJk4aqRCdBmD/VPUZ6jfgNdWAzDHFkrwntWWtC6eHoHabGJTokSmM0ocvhcGD7YOchFKFCYbbhzOKKY3+lW+Zfp3po2irKLTOulHDG8vj1NjcFOcy8Pf70QRFD2AXSiPJK34zqT6YRilNXFUTXNthf2g2bTRwvHWTeMd583zQfMB5ynpjegd2RXMQcI9slGnYYfxbn1FmS0RDqz1TMLoovx5iF1wMhgTh+JPvzeTg213R9cmXwLW3W7HEqoaiupxPmEaSPY6Xi52I3YfIhcCCEoSch/GHm4q5jBCQy5bGmuqiaqQUrlC4lr+wxpbOuNZF4qHqf/Tm/10KFxJCHFclai/rNqFBDUc6Ty5Y+l0FZEBnWG7kctZ0P3f2eqJ87XlMebl5Unr4dsRxFW7saiRkaFx4WD9OPUYBQTs1ti5JJyscXg9fBhj+U/TB67PjhdgNz/fJRLt+t5+t5qaXoWia6pT1jkSO34cah5eEHYTogjCGnITViW2LcoxGk/SYnZ4BoeGtZbCauIjBRczx1BDet+cy7nb50AGlDAcY+CBAKL0zCTwzQZxLalNQWvVfOGg+bK5vLnI+d6h56HkJet56eHjheI92InTWb29s6maoYSNZIVS7TJ5DNz0NMq4oGB+hGCoOxQIS++bvQOe63RDWX8p5xCe53rKPqvSjW501mBeTbpC1i5eGaIeGhFuDCoeZhh2Jqos7jSmPzJUimyCgzab3rL+19Ly2xXPOy9Y64SbqRvRf/v4GQREzGx4lzy8/NVVA8kinUE9VX10BY0Vqz23bcYNzBXiZeZJ8UnsDfTB5YHc7eB108W7UaoRj0F35VjZRUkpDQMw3jS4fJo8bLRRjCFYBkffg7Gfi69ra0erHsr/Utqas7al+n06bHZdfkhqLVoi7iP2HkYIAhFCH4oYahwWLoY5Kj4aXyprbojqpMLLvt5XBW8w/1AbcHeVE72P3ZgJkC3gWnR7zKM0zojriRdVKw1FzWnRij2Wua6dxtHLGd0x5DXgge3N57HpKeVN4zHTFcLdr1WgAYTBa/lZYTgBEaj2+M4YrryEoGMINwQN0+iLvWugg3prUZcx1xJy6uLLLq+KkVp/6mNeT1438i5uJXoTMhqqGfoQ0hW+GpIqNjPyPuZTimBagnaZzraa0xrvWwyfPgtVO3pLrNfMA/nMHIhDsGKYjuC05NwM+hEfgUApV4Vr1ZP9lPGzjcL902XfgeKJ6a3lIfER7g3ejdV9yV2+pacljp17CWPVQnUlrQbU4wzDVJngewRK2CbAAO/ee74Pk6tqg0CnJBsIst9Kue6iLpHicy5W2ka6PjokxiGqGaIRPhv6DT4ZKhzCKKY03kiuWiJvXoiCpwq/Ft/K+M8gL0XLcoeOj8JP3LQC1CwUWMR8cJmUx9jqMQwFIRVJBWRRhVWVgayxxx3O7dfN4J3ogezx+Pn1PfLR1YnTFcLVsj2n6Yghc0lUsTP5FOD4LNpkr+iJrGTIOFwWy/eHzQekZ4pLTn8wnxCm8V7Z9rY6jXZ+bl/+TH5BTjDCLm4bOhNGDZ4Nphs6FMYd5ioKQL5bwmfmdBKXIrCazX7s3xP/Nk9Rj3yTrCfKB+6AFOw6eGz0kri2pNOw9M0ZpTsBUeFviYh1pG2+2cDRyN3ZCeFZ7uHuvehx7UHlkdGJ0HW50bBplLF+dWUhR10peQs46IzHNKJYewhRGC5sE5/UQ7lLkIdwg0O3GcL/utkSxQKkRojSbOpghknKNwYxWhiGGtYOXgu6De4SChpeH9IzVkTeVIZ3yoj2nNrDltg2+IMib0TLZH+Rq7/z05AAhCDAT9BtLJwYwXTnSQZdJo1FFWfpecmMta0Vu+XVkdeR6YXgifIR6knwYeyx5bnT0cvBt1WhHZOxbD1bUTZRItj4zNrUr2iGwGRQRXAdc/TDz1Omm4O7UY80FxnW9g7jDquClGaA5mQuUbI5ei+mG0IVehRGEtYRWhKuE0Ik7iyqR/JCsmpCdPqVjrWiytLr4wW7OFdSn3YvnSPCs+7EDwg6NFzokjyppNXA+8UMYTDxUqVpdYnZpY21YcIF0RHapd+R63HvRe8R7gXqldcBym3Bbay9mAGANWdVSM0iIRLY65jGmJxUhthamC7wBm/kN7uLlV97F0PLK88DCuRSzSqvborqcL5dNkNaNvIsJie2GnYXSg9KEYYfPh2WKUIqokAWUO5uiogKoFK4buKu9vsgh0CLaPONT7D/29gDoCdcSAB82J+QwUzarQMNJQFDRWahcSGROaaZt63Azdj93iHm6ev97WnrHeft5inSXdBtuTmhPY/Vca1aqT8ZI2D3+OJQvASRGGtkQ9QUW/Bv3F+1w34XZQc+txpfAObSwrkOnIaAym8SWro+hisOKboSxhvyFfoQ+hPqGJYepilOPDpDMlJSeGaWLqAqyzbpXwRrJHNKX3S3liPFu+FEDOQwuFq0jaikZM389CEWxTJFSzluuYLhmi2wJcH9z7XUNeqd8zXyweI96wnjfdCVzKXKZa+Bkc2LWWihUL0wDQ5M6JjMMKWwhCRjuDp0CYfuZ7jDoX92L0bTHNMEluPuxNqxcpfebfJhAkZKPhIyQiCWEc4VehVCFloWlhhGLoIyqj0yTx5t0nnumdq6MtYK9YsUbz1vYDuHy6h3z7f43CxITJR3NJFYv/DY0QGFGI00MV6hdkWAzaFlueHK9dsZ4RHoBeJh8j3z8edN3NXbOcUhvRmlSZfZd/lVjUHpH+z8/OBYzQicLG6AQFgqW/qL2QO534iLZJdCpyJa9YLXzrt2n15+bmT2WJ5DsjXiK7IemhWGEbIQNiDiF+oqXis2PnJMDlWGcbKPlq9SxK7hqwOXLX9O523HkY+3l+KsFzQqQF7AgzSgCNNQ8YkHaS6BRhlx1YMpmQWkHcFl0p3bbd1p7+Hqhe/N7s3eidwN13W74a81m3mBTXYxWKky5ROQ6LjE6LuwiEBdwDsACsft18dfnxdxk1GDLzcTHuPmye6qLo9GbLpaGlJyNcIr1h+OFTYQfhHWEs4SghkaI94pCjuqT3Zv7nhCnlq8ktEy8gsaPzpbXQN/55wj2g/zAB5URHxs1JVUt0DW+PRpIYU96Vtxd92KCaVlv4nFdd2d32XoTfAR85Hude8x4+nWIckJwk2o8ZYFcBljiUT5IWUJUOFYvSCV/HWMV2ggxAcL1IO2T4j7Z6tCIyGC9WLcisdep+qEZmMuUVZGDjdyJ8Ya3h/KDfIE7hCmF1If6ibmMyZI0mPucWqLjpwux/rdewOvJMdJS3OfjWe6y9s8C7gwaFbAe9ik4MmM80UIpSkxUxlicYA1lE2oXcKZ0uXW/eOF713qHe3Z6vXmBd4R0nHHpaQNoEGImW0dVOU0jRJw9RTRkLBIkWxjLD14FlPsl8SDq0d2X1n3M1MO3u7Gzb6tHpGmdcJoxkUCQKIvrhyWGyoSkhAyGq4TphhSJtoycjQKTj5junnmm7KqEtLW798VGzbfYvOAE7A/wLfs4BtsP6xoeI6wubzYSPtlGfk0fVuVcbWL3Z7xtqnI9c4Z4e3lLeux7xH12e/h4KneOc7ZvdmnBZUte01rfUoxN7kFkOKExMShxH+sVlgmBAlD4/u2O4+vZ0NCkyF2/KbdVrkKnPqEzncuW+pJTj/SI94cehiCFpoVYhkuFBImYipGNxJOnl6yZKKM1qdWwqLc4wBTHOc9z2IPjB+4t9pUBAAxAE0gdhidrMjI37ULYSx1Sc1oJX79lim1Obl5yPHiGeLl6rnruexF6inuieJh1F3GRbL5ouGIBWldVwU3KRHI/3za7LcAhJBh9Dw0HCP118onr4N9i1ZjOpMRqveWzjq0lpcygpphMlBaQa4wBi7eJv4hyhLqEg4N8iU6JRowDjh6UpZmanpak8KortIK7q8OzzVzVEt+E6YbxffyJBeMNGhkyIvQshDTBPNVE3UpDVZtatWC/aBVrjXEhdFB4b3myeaN4qXusejt5dnXac1dwLG2IZ+Nf3FfwUmFIYUAFOoQx5yl6HukWVArBAUj2J+7G5ojcDtFey4nBYbgnsbSopaOemyiXj5L7jjGK7IYrhUiEaYSYgwuFzYgbi6WNmZChl76duqLJp/CwvLQRwD/FUtEj2U3iJ+yK+Jj+yQ1nFGcdRCSeLm838kDvSBJQ4FZIWztmo2p0bYB0pXYHeNx6S3vBett6rHojdyh0PXKbbG5r2WVZXHxWkk9nSaQ9JTijLeQkWRwKEKUHqP0u9u7souHR2KzNCsW+vLS0kK53p6+gBpgHlVWRyI6VipmHkoYch1CEpYE5hsiJXYv7kIST2JgBngKiCKzbtDu8ZcMOybHTnt916Jvyyfw7A9IPaxb8ItEosjNRPLZEfUraUl5cjGLTaFJq2m2jcuJ2jnmPdy58fnu/eRN6gXdndOZwQmrdZ8RdpFjZVIBKTkMoOCUyJCmqH+UWkQsFAzf6DO9B6S/di9MFylvACLw3sTOqw6LPnfKXF5SWjieLI4gQhkqEL4TPgn6FK4j8if6M+ZJjkymbR6EiphuuzrNavgPIYc9O2bbh0Oy19l0AQAmtE8sb9iP8LgY380DSR61PkFWmX5hkNWhJbbZy4nWReHl3AnvAe+R50npAeJp0VXMGcNxoEmMWXHJT+U4LRyI/9TakLmAl+hthEi8Iuv9w9iTtFuJ92WLOQsfovtC1La5Pp52gQJsvlUyQFI4cik6H1YW8g5WDyIW5hZqH5oo8jy6SdpsWnWSl76tHsnm4WMNMzbPRat4/543vOfpzBH0N8Bh7H38qmjR8OFxFAUsrU6ZZF2D4ZUZt8m8BdIp23XiMe6d8UHvNe5h4onf/ckVwHW10ZclikFunUxRNn0WbPZcztSvcH5UXFQ39BDD5x/C25mfd4tJTyvfCN7p0r6ypWKQDnYyaE5S5j5WLlYjrhXGCeoQ+g8+FqIUfieeMYJL9k8Sbgp+kp9WsjrY5vZfEp8wh11PiiOoX9YEAfgY7FIEbiCVCLlU2HEBXSA5PGFdEXrtgHWckbuZvB3andx16UXwXfEJ7C3uSeCV2vnH1a4lrD2NdXzRYA1GhR9FBCzo9LoQouxvnE+UKUv4h91LtMuMm2+/OLMjDv5O5wK9bpwigPpxMk9SQro1xifKG0YPyhQWDgoWEheyGNIunjO2Tw5XenDCju6cos7W3PsOYyinTs9k85znw2/ZWBNoMrRYBIqooRzLlO05CcUjnVNFY4l+rZW9r2G9zcTl2O3mLevN7Ynt9eS15pXchdjByN21dZ01h9lsyVlVNSUeFPvYyOyu/IBUagw6CBYb7UfJP5ELgvNT8ykrEArw9s1asT6Unns6YX5SQkN+KP4sAhXKF0IHvhuqDi4UOh4iL3pEFkZeaD6ADqImtbbR5vFPFtM271Y7hq+m48Hj7JAazDtEZMSRbLf41dj7dRQJOV1fbXKRhwWrSa21xWnUzd1B6aHl+e2B7BnlxeXh1p3Xvb/pp3WNUX2lX/VGRSGZAwDjEMfIntR7+E+UIsAA+9TfuGeIo2rvRFMbRv9e2Ba+BqBmhd5srlyKTiIthiFSI84XXgN6E5oPkhf6HhIwEjSCSF5fUnF2i4afMsdi4EsCeys3SE9uB4yPurfaHAYQKMRUIH5kn/DBjOZFDZkuFT1BZ+l4MZIdqJHC8caZ1uni+fNZ8z3vPe493F3dddchvIWu8Zl9hZ1w0VX5NaEOnPd02pinjIWIYQxBlBZb9lfAc6bfg0dYUzkjBWr51s6irUaVln1OZcZghjzeMT4kJiHCFBIUnhBqF44X6h+CKLZKdlO6ZIJ+mpLStFLL4u4DCEs1n12/fVeh68fr8hQTVEL8Y8COZLVg0mzwmRTFPnFMTXFxhVmgma/dx7nIDeKR4wHr9ekl733cqejd1PHMDcJZq52TyXRBXclJmS4lCejljMF0n/x5AFQEJwwLN9lDwIOOp23/Sbci7wJS3jrGzqY6gF53ZmMSQuI41iYOG9YaFg32D+YMXhsGFVok8i3yQhZUGnNmhb6d/sI64k7+Dx+TPzthG5MXr7vWh/xQJ4xVeH9Qney3MNzpC80iVUENXhV5bY5JqhW7Gc0p53ng8e6N6A3oVfSx5vXeQdiVyImtjapJivlyKVgNPH0SKP3o43SxeI+EZoRDSBoH+qPHP6vLgONafziLGYLy3thqwrKZLnjqbEZM5kE2LrInDhcyFGoijg/WDTocMiiyNqpBhkmyYXJ4fo72t6LNQvS7D9cqU1T3fvedj8T/6tAJwDpIV5iFZKxs03Dw+RGtMyVQVXLdhsmc7beNw8nSTeKR3MXvheYN+xXgrdw52c3aucMlpyWa8XxhZdlIASfhCRzq4MBUohSCPFNALHwMg+sPvKOZ73FnRf8lzwX66HLM/qK6kMppNlf6Rfo+QiweI2IcshQuDe4S6hmmHTYjmiuCSEZMHnfyj3KhjsPC2Zb7TxUbPvdn14SDrr/Wf/70IORJ7HUojwy3MNqBA9UeDUEhYR158Y35rK28Qc8d22XYIfGh7nX1re2l6C3cVdu5voW2naWpm712GVjlPdkjUP0o3cS5CIy0ckRPpCED9wfVw68rg2dUGzuvEEL0ItWuuvqWKoQeayZXYjzKKQ4e9hlaFJISeg3qELoZBh7aK2Y+mlNCWfpzNpSysH7D8ug/D8so/1Rjfx+he8WL61QFHC5AWbCF+KCUz4DnNQ8JLUlQpW2lh3mXKawxxanRHdlh5kXlZe/16cHs4eu92Snaobhlr+WjSYQFdfFXoSfJErzpXNRUpNyCKGcwOwQTz+wrwLucq3h7Tx8vDwsK3e7KVqu2hiJy7mM2T0ozmiYqH0oTdhXWFloN5g26Hwol9jTGRw5OimXqihqQHr0S1TrtBxvXOgNfH4QztnfR1/vgIeBCRG0Ylny2qN1lBXEdwUCBXF116Y8VoTm4CcyB1DHh4eqZ693zfeeF5f3j7dJRw4W5laspjf1v/VrFOg0hnPsM3dS9zJq0bdhElCtwAMvSv6y7iq9eR0DLJmb6Itguv0KgXo8eZ/5RVkyaP2ogyif2FuoNXg+iDuIV9iACMd49ik6qWkZtzoeOqOLELuEDAwcsy1Fbci+el8Hr6MAPrDcAVRx4NKToxNTvnQ6JJ5VGvWp1gV2aAalhu1HQud256g3tDe8F6+nqhedJ2+3ZUccJuXmcUYGFYsFVfS+dDwjzIMa8qVSJAGJAOxATc+lTy3OZ33h3SQcvWwuK587Jlq4SlOJ88mbyWqI3xi7SIAIZ1hVmDXYP0hlyFoogPi+yQFJSzmuagR6UzrDm0+7tvxrvNJ9cH4Yzr0fOn/FcGEQ/eGkYk5SwvOAI/G0exTpFVs1syYU5oB23icEx0uXqnelh7H309e6x8SXo5dJd09G2HaYhjsF76VzpPmktvQM44cy8MJlgdcBNkCeUAcPat7prk0Nrl0GLIlL9wuHCvCanuoGCdcpc4klKNKonsh/mF1IKchu2E6oQchxSMi490ku+WXZ50ok+pALJzuP2+P8of0p3Z8ORr8P73YgHmC40UbyASJ2Ax5Tb4Q4VNu0/BWKliHGWoa9hvJHNdd/Z3Knslesd4l3tdeS95HHUachttLWi9YNNbllQuT2pGcD3tNB0tciSuGf0P6Qan+sjy7efQ3mTUKc4fxCC6ebOvrDamAp3VmFKSSY5FizSLtYUfhSKGp4SVhLKI7YezjSeN3ZORmtqeQqaPqv+zhburxOnMMNfV4SXpNvRv/MUGfRA4GokjdCxmNPA84UcxT89W11z+Y2RoSGxHc5J2Y3cnegp9Y3s3e8Z6hXnwds5x4W9sa2NjD16kWTBT2kqSQfQ5hjEtJukeDxYOC40DKPkd7eTlKNsG0afHJL9/t86wGaj4oPWbEpgukLONHIl3hmKEAIW/gxmGs4QyhrqLT5BLk5eXC5tco/+pH6+4uY7APskb06valOMe7T/4WgFeCbcUVxyhJ84v9ziGQMNKGFF9Vz1fiWabam1ugnNmdWp4mHkjeO58oHqiekh4lXQ+cD5tNGhTYlFbVVVBT+ZGKD+aN3wriSK9G5QR9wXt/KPx/+k24ZXWWc0Dwne7L7UHq7CjgKANmViUSY8xjjaI6YUYhuWEzIQlhXOG+IZLikuQTJUPmhieW6QXqyix57oCwzzKStYR3gXom+8r/UkFDRFFGHAi0iu9M848A0Y+TV1Twl1SYaZosm10cQZ0oHcKekF5FHvieiV6NnlHdxRzn3BfapxisWFSWDZTBkq+Qds5gC8GJzMf8RYPC28CsflL8EbjHN2C0rTIQsDYu5ixnqk7o0ed+pflkaKM6Imoic2EsIIeg0qFzIRSiC2K5Y7yktyVfZ10osWoyK29tqm+E8j8z2nc+eAb7l/2/f99DLISFRvvJ+AyEDnOP2JI6lGVV6Nf52N6aXRtX3Rudqp3l3juex5+GXqdeXt4BnW3cuNs1GbwYu1d5VZsUHRGRT6ZNNstgiPjGn0QMAZn/1T2PuuG38DUZ841xje/07WsrNGnCJ9dmu+Tx4+4jcaHxIfnhQ2F1YIJhYOG8oeuirWOrpRmleCem6XPqsex9rm0waLL79O73T/oefCw+iYE0gztGd0fHyn8M7E8nEQpSvdURluGYS5m+GyGcQJ1+nVEeKd553zMe5t7ZHjjd1R0WW6XasJoC2FlV5dRskwfRrI7lDTPKbMgehcQDDUFZvjT7n/l9d3I0gHHNcP3u66ww6zbpa2dR5mDj2eOJ41Ti3+DKIWlgWOFtYX7hhGKV42WkEGWn5lHodCnUq9FtMO8FsRaz2rYu+O961/15f3kCEsTbhtHJlktLjnmP71H+05gVtVbMGKUZ21ux3GrdkB2nnspe8F893tvebV4b3UvcmZvR2vZY6RcoVhHT5FI40DdN7svlihwHNoS9wj//tj0Zuvp4STZwdBSxwXAz7VDsDumAaEVm9KSZZGsjzuJN4anhBCCDYR1hJ6ElIlLivqNmJLwmHudMKR/qhCwtLnXwLjLudTg26znU/Dc+U8DiA1zFaohXinoMWo9uERhSCFSIloPYt5mSmyCcC10VniXed96H3phfEx7QncodxR0/nBNbDJmJGC8WmtVMU/lQ8Q8BjS2K3ggCBlyDwECifmw8j7n2dwa06rKb8GZusGwmKrcpsKco5ptkzGQhIsRiCaGUIXAgVWCoYKMhQWKb4xkkCuXe5xnoDenyKy4tUm9ocSS0InYjOAK63LziPyYBuYQxhozJG0tUzYEQJRFD0/zVFdbHWQ+acRt9XHWcj5443jqeZ58/3tCepN5mnWqcjNtKGqUYrdd61qKTp1GmD+sN6wufyW3HZoSewpi/h/1vuzA5H3YcdFYxra/+LZ5sKyn16EnmsSXVJJMjYGKqIYQhSKEo4QChveFpoi2iWCMJJUXlkycPaTgqSCw+rhlwEHMOdEq2lHl4O7i+KsCwQiUFAwgdiosM9k6zkOHS8hSyVrAXg9nr2t4b/FwoHXoeT57yHsLfJl8KXYIdxN3GnGMbVNnLGCXXQpTAE/oRGQ9cTM3K30hhRjjEYMH1/ko8CTonN0h1YbLEMW0vaSzWKv/pTqdgps0k52PqIymh/OIJ4ergo2DlITLhgeL7Yxxjf6UMJuhn06lk61mtcS9Jsbgy3TWqeDc6sPzEf3FCNsQhRvYI2otcDUSPtlFhU2mVUZcDGNlZ7NuD3EJdAJ203jHekZ7w3z9eXV4UHZcc6lvSWvtYYVeMlrrTGZI5UE4OvMteyUtHx8U/QrmAaj3se0m4hTaG9FxySrCvbYcsSyqJ6OUmxqWE5S8jLaJs4d4hMaEAYWng/KGlIkoix+N7pMDl8KciKE4qs2w/bg9wgHIINEg2Yzlqu0X9kcAFAx9E5UdQCm8L7E3bkIKSkBUU1gNYRpkVWohbs9z0XQzeY54t3xffWR6Nnpid312c3JYbUlotmIQXPBTfk46SC09EjZdLCkjJxd4D3QF+PuY89noaOBN12nM5Ma2u8CzyazIphyeyJkSlgqO0YsCiRmGzoZghMSGC4TFhjGIc4rYkL6Us5YsoSik9KsUtIe6U8TUy97W3d0x6Snx4vvlBo0O6BkmI6wq3DVcPHVH90wZVHZbgmKbaORsVHI2cyd0FHuTefJ7Xnm6e1l4GniicV9vpWn5ZQtf1VokUqxJX0J0Oa4xxSd1IEIVcwsTAfX2gvBL4u7aN9IrygHCsLbDsLSp4KFIncuU5JI7jg2LUIiOhzmFDYT2gsqGwYjSimeLZ5DkloKcs5+FqY+uZ7U+wGjEl9A13MDicOwX9ogBagrhEx8cqCQPMvs2/kBMSBdS1VmKYBJnUWr2bu1xsnd1eB18GHtFeiZ5KnsldSF1enOLa8FnsmHTW+BWhE3HSOo/sjbBK7UjKRqYEdQKEfzc81LpceBY2D/O1MRuvUy1Ka3YpTugv5sklpaO34yhitKF1oXtglCFBoYDiICJ+4yejY2UK5gin62j26zAtFq6tMQgy87Vat835y/x2PlnAwYQShfqITAsUzKyPXpEBUyhVORce2G5aL5srG7OclV2wneCe5h9rXzre/p5EnYidLBugmsFZGpfeVylUyFNtkKwOOUx9yecH0oWYA1aBIn5s/Gx54PbRtQ8y1HAP7i8sSKqFaO3nVuZApTUj1yKuYklhfyDaIIUhQWG2oZWiTmMaZCdlN2buKBWpvSwxLVJvjHHT9Df2SXi+Osj+M391AgnE7UcOiT7LgA4y0CVSbVOOVkBXsRmS2h+b+lxw3TueBl9wHoSeqN8kXmidld16HI2bMlnVmJNXAZWgU/WSR9AuTNpLZgjIhq5EVAJJgD89DfqEOE62h3PmMjovAG3Ra45pvqf+JhOlBeQx4sriM6FjISahSSEaoUrhSOL3ombjq+VB5hpm1On3aqusJC6IsNNy+vTw91Y57zvBfrsBJoMPhfRHrIobjLHPKZFdU0qUx5b8GAVZsFuOXAKc0R2V3pWevl853tXeV9713jtdLBxMWmpZVRhQVkPVJpKPUP6PL8xTCmuH5AXJRCtA0n5k/G75rDcdtTKyKnDILnMsoWqLqMRoJqXjJJ8j0WMEYtmhFuFXYV1hT6Hboa+hwmOU5F5lBKbap8DpoasIbZ4vfPEIs+D2KHfJ+th9SEA1QdhEsUZ/CVMLDY5NkBVRhhPU1daX8Zk6Wfsbnl0jnVNeMx39XoafU18anvvebN1gW//ai9p4WNHXzdX30+jSeNA6jjpLuQm8Rp3EbcI0v0u9RvtbeOe18HP0cgLwN613K8nqZ6gr5rTlNGOE46uiYCHXIaXh8eDv4VqhIuHHYrZjTKR05cEnPigsqubsai7h8F/yonTwNqv5TfuP/i+AqgNsxYcIBUpAjEWPfZCgk0SUhdZOmBAZpJpaG/4cp52OHnPe9J7gX1HfIB4+3fYcS5x8GpuZwdh+11nVjxMQ0QmP+wwZitHI8cX+Q4IBTn8+/Fs5nDcMdffygXD/7iBspWsMKWNngCZNpEzknuLwYfbheGE0oUehGuHUoaWh9+LrZJKlaSXXZ41pzuuS7WxutTHms7J17bhy+k/8+n8BgZ2Ec0atiF7LYQ2QD5dR2xQFFR/XfRgi2jPbAJzhnUReLl6AnyOe4J6a3mreVN1yG8zbH5q2GOvXatYBE6lSfdCpDagL5QkyBrEE7IJogA895zr5OOx2OvTG8oPwFK3M65Gq0+hmZz/lDqTxY4RiwuID4WBg6iDcoVkhk6KVYlyjYSSJpfRnuahxKvQsB+418G/yeTR6tw95ATv0fh+BLoMnBS6HtsnMy+xOHBDp0tWUoVZFl16Zl9qd3DUdIt2OXiIe8J6Vnz/eul5+3axdMJwJHBWaI1j8ltWVsZPrkZHP+M16i3fI7kYCBDaB537W/EF6J/g4dY5zgXEkbuvtGus06Lmnr+Y7ZNqkECNAoe3hlKFhINxg5GEPIdNicaLXJDLlFeaC6ASp+is5rTTvJXFV84b1aHfHuhP9Lr9agXhDgcZoSONLNs1RT5tRUFOg1YfXS9inWhFb6hwFHJJeIB5wnkyfaR83nkGeoh3xXLSbvdoxWXPX5BYBlFWSsI/IDnkMJUnKh+CFPQIrQDb91vuw+Oj2RzR48kYv7a3mrBFqFyhiZ2DlkWSrI3/iMWITIZkhUOFBIV7hFuHZYq0jPGRG5e3m16gxafhrpK2vcIByQzRvNo/4/brhfUH/7AHsBL/HSgmMzHQORBCDEmzUvFXxF5pYpZoEG4vdCp453UIe9h7I3tTem556Hg/c3BwO2qKZwplyFxhVehNOkYGPjw0siyJJGcZYQ43Bvj8u/Jz6GHh8dVdzu7DDLxhs7KtvqRon0aZs5TWkJCKpYjYhE+F7oI3g9uE0IVlhsCMBZCCklaY9p6wpZmr47Fuun7F7MuB1BLdjeVs8aL8PgWID0YZtCBvKl40yj0pRQpPtlPYW+Bgg2XpavFv0nQweQN5TH2ufZd9PHsCeSJ393N8buVqrWZXYXZXDFGaS5VEiTo8M/kqRSCSFvkKoAE1+RHvpOON3IbSsMhEwaO5aLA4qZaksJyaluaRsY2+irqHVYYFhq6FooNChBGHaoloka+RjJUQnBSjD6gSr4G4Lr5PxNLQAdx+42Dt1vW1/T8KEBR7HZ0moiwtOLdAxknUTyVVC1/gZRRpzG6tdFV15Hl8emF733zkeod5JnmBd2F01mszaThjplxUVV9OY0awPxY39SxBJjMa7BLCBpz+xvaC6krhhNYwzknGrbyttnStEaaInl6ajpXYkYCP9IoxiLmGxIJVhbCEXoahh2qKi46Uk6yWGZ6DpbOqbLHWuQnDvMic03Hf4Oc679z6EgRjDewYqB/tKZwzGD0MRcZNoFLLXCliGWbra6duG3WxdRx5vnpLeyV9+3mhePB0bHFWcrxrb2UtYI5bjVI2TGlDpDnTMwktNh9FFowOwgTs+N7uEubt3SvV9MmpwcW4g7B8qnemDJ4LmISSJo6PjMiI64g3hFCDN4RMhbeEWIngkG+PEJVpm3yhzqg9sDy2T70Yx3jPUtmd4hvqKvUT//gHbhHwHI0mQy2bNwRAokg5TxlY1F0NZZBpDG86cZJzIneueut8GH1levl553cVdYVyvWysaPZiXFxNVtVOmEgLP3M6EC/RJfUb2BN6Bsv/L/UW6+ThLtzuzo3Ho7yftcSrTaYhoZadiJeEkE6MZ4fShv2FD4Mlg4KC74UnifeLBY73ka+V6p36ow+odbL3uMbBXsyg1BXeyedD8Aj7MAMpDH4UFh6MKZQyPzxWQ8FLAFT7WDVgrmjIanhuWHNpdXp4CnujeSV7E31YeiF2N3F/ceRsxGasYqZay1OVTPNFEz05M0opkiK0FxEP9wJc+0TvTejl3enU3MuIwce5DLSWqv+iXZ10lhGUF5DNi5eKhYb3hUmCxIP/hPWF84lZigqQdZR+m52fTqZGrpq1470XxpjMJtaw3u/owvNn/M4HCw/vGa4kKC2YN00/e0SbUC1WVFyNY5Bqsm2ncwB3gneceZB5VnvueqV6E3jqdS1ybG5+aS9k1F0jWL1STUnuP+c3ZC39Ja0aoRTZCtn+SvWi7VXirNgvzjrIa8Hutj+wwKqMobGa6pWdj7iPWouvh8GEl4XHgwKG9IaOiqKK8ooKkfSXQpy5oxWsybNcuYfBvshP03vcDuVL7Sb46QFhDDAVnB0+KqYy/Dz5Q7lM3lREWspfVGaMaxlwS3C3deB52XsXexR82n1ueq54oHRCctlsoGgtY3Fbg1VmTuZEhT2dM/gppSJnGKAP5ARQ/BjyhehS3jnV7sv3woi9V7PaqQmmEJ9OmbCU844xi9mIkobggxmF94S2gxiHXoj6i3aQm5WOmayga6YjrLizQbw2xazNHdak31Pq4PJf+3YHexFsGnQiKywaNiA+yEYtUHxWllvFYjpnsmxxcFt0u3c7eDV7zH1bept9unhEd19zMG/dagZmeGByVhtScUrTQZY4si8vJzkeiBWbDMv/wvXD6z/lrtiy0AvFX8BlucOxv6ljouabLJfEkTWNvIqJh6KF3IQRhG2Ek4VciKKJL4zckHmWNJmrosKpnbH4ttXASMjo0T7c5eSw63b4rADQC4wUgh39KB8unzm+PxJMu09bWE5fLWafawtujXHGdZd5hno6fOZ72nwaeut3TXQzcARuYGY0YShcz1RPT9tGfj8TNZ0sxyA1GyAOvQiJ+xHyuuph33jXv81zxJi7a7SCqxmoAJ6lmbSTApA4jHeIx4akhaCEzoRLheuHJYVmi+CQmJW0mLeesaV1qV+0K7s5wdPO+dUX3yHp//Gk+nkFgw5GGYUhzCpmNSE6CUXxTQdU6VtPYVxo72xgcmh1GXjbekt6zntKe7x54HiQdSpzr27WaslmiF8UWalS40pGQ6U5oTGFKDweLxWsC3gCV/gy7vfjB9p20SvJ8sDcuKSvRqk6osKejpf7k1+OD4vyhjmFW4PvhDGDfoaFiHeLD40vkK6UWJvCoLuokK8zt2i+5Mex0uPZWeTI6Sn2nv8/CkgVkhvgJ3kwLDnQQLJHpFECWY1ee2UeanNuRnF4dkd5EncGe416mHvPezt4GXXibuFtuGnfYuldB1UTT4xJFj7bNq0u5CV1GOAP6QZX/jLzv+rL4Cfas8ymxrS8m7WwrSSn/J1ZmYmVE5D0jKCJjIfihM2DhISIhUiFCYo8jUWOLpSLmm2gV6Ztq2GxMrqOwfzMPNS0387pIfHx+04FZQzbGHwj9CrpMgk7VUU3TopVuVkNY0RlVGwPcJNymnb8eTx9AHs/fJl6y3jndTB1DnBFbOllll0LWqlS5UwTRL46FDRAKkQfVRdCDoQFfvrO7Trka9zv0qHIFcH5uquxrKjKoSGfHpiDlBuNmIseiJ6FZoM3g2+FbII1h7SJlo1jkkOWV5r2of2m0a5tuK6/acal0UzbweOC7M/1GPwpCkoVOh48JpAu7TZbQ09I/VG/VzddSmYTax9td3HgdB94hHmRe756fHtsef56SXQ7cjtuYGpNYSVdNVbjT7NJXkDWN7wuKCUCHJYS2wfs/6T19+tZ4mXZGsyhxmy8M7eir1qlTZ28miqWvZA4jjmKbIYlhbOD/YN2g6yFKYriiwyQbJJKmEGeU6UwrF2xvLqywBrMm9Ea3wHoU/HH+RwEsgzjFmwf9Su8MlI7/kTvS39SDlroYCVlvGxucTtz3XeDex17mHqfeVh6Xnzkdzd13W//bUFpwl/TWApWz0oFRVc8xDLCKsIflxbVDD0E7vl372TlzN2c02XMQ8Lju3qzg6pepASeRZkMldaOOIsJiZSHy4OJhD2Cb4W2hXKJcoxVkSOUIJw4nz6oeK5Jtcm+PMXJz8nXAd6m6yr1j/zLCBETbxo/Jbou5DcUQL5FYk2WV61cdmOfaQptSnEOdcR3S3tWeix8dXzaeT1323U1ciBuIWhWZTRev1mgT1lHsEFEOMUvViTLHNQShAgYAKH0veyQ5IPaatCkxi7AXrVZr7imnaCdmqqWcpGSisOJQYeohB+FyYT2hAiHloc1itCND5LSlsmacqAhq2+ya7lTwfXKbNO+2eDj/u9Y+dADdQ8/FckfcybgMpc8R0X5SWRTm1i7YPFj8mvLbxd0jXYMeSF7Anl8e7t6anqEdqxyCHL1bXxoi2CYWqdUFkuARLw6GDKBKmUiARp+DqsE+/qB8GfpB+C804LMgsBmu++zl6rxpqudrpiKkzGPIoujh3uHroXhgCWFMoeQiJiG7YkDkT+Vapq5nq2lNKwrtc+9IcM5zwHWyeCn6wr2Uf4rCDQRJxxgIqIs5zQVPklJLE80VTBdUGNmauNtanDydUN2SHn8eqR5h3nxeWB4SHdBcApvcWt0ZK9emVjDUM5IrEHJNkQxNSWVHfcUdwrZ/hP3X+th4VHYHNADymy/bbYKsEmpYaHNmt+V/5EqjUeMCYbvhmCEJ4RVhOWDJ4VKil2OcZImlgadF6PvqUGxy7fSwBXH2NEG2t3ldu4C+NMA3w2UEnMdfSj0Lzw4H0SpSbtTBVnuXfVjc2zGbqZ2Yne7d+173n0wel15d3qKeRdy03J8bJVmdmFBXB5TXU4sRak6mzTVKgsiURnWDsUE+voP8/3pW9+i1fbL6sYuu/Sz76tupXGdmJo3le+OGI1Th2KGn4NYhDyCGIT0hZiIkYr4jlKSApnnnkamlK2HsmK7JcXNzWDX7t/n6fvyB/veBboN6BrNIQss1DaGO4lGvU55VLta82NVaDtu8HFSdrJ4x3kIfNh8PnkueZ93tnbmclNv5WfuZVRfnVhBVHJL50ESOtcyvSatHWUV0Qq3AO70ge3Y5uXZxdJnyXbAyreJr6up/p91nN+XmJCUjZ+JE4a7hqiGtYPshB6FJYn8i1COtZF2mNibM6IPqgKu2bcXwHXH5tBN2xrjI+z++EL/NA5cFBEgRSYMMMk350HmSY1Q3VevX8pkWmohbQh1VXYheIt6lXtjfl57jHm5eA5zWHE3awxpTWF/XDpV+U1HRPo8pjUoLnEj7BrdD04GhvyN8+zpjd9P1fvMb8gLvUW1xa25puSg75tUlUaPD4xXjEiHG4RBhQqFYIOhhRWKvoy8j2OTUposnrSjHquxsgG4ScM+y4nVBd8D6JzyEPwQBmcQpRjOH9UoLTXpPfpGJU3rUpFaGGJUaD1r629WdhN3d3v2exR7xnt2eKJ5MnYidB9xXmxuZddfL1pQUkJM0kHNORY0TSmDHVcVYQ34A4/3k+6w42/afdNryBzBRrkTsFKnpqLRmsiWfZGUjRGK/Ygphm2FbIQlh0mFPoZ4itONlpG9lmydpKPPqautHLbQvZHK986/2T7iHu0S9JP/8glLFXcdFiTsL5c3KkEUSXVQt1dUX0tlrmjtbdtxJXdndtR6Y31Bfoh+XHmKeCZzZHMkbl1q0WEaXxpXeE/IRyY/PjY9LcIkiRoTEDAFpv509ObsTOEU1/XMMsadup21u66RpmCgCZrqlgmRHY5pil6FHYXMg6eE04Xvho2HtopUj1+TBJsBnqWgRKs8sky4I8FJysXTvd0v5qXwt/iaBZkOEReVH44rEDNDOohDy0tBUx9aDWAdZ8xskG9ucwd3injzesN6L3pfe5F5CHZLdEVwuGp5ZyxgMlkxU4tNmkOPOngyESnxHmYVoAxyAwb5k+815sLcj9LkymjAT7nMsIqodaQ5mp6WTZDEkF+JK4kshSmG5II1gySGcYbsiI+MYJJYlgucZ6H1p/2rEra7vRvIMs5s2G/jYu0s8rv97gaYEbIcFCdjMT01c0HKRv1OAlfrXipm6WYhcD9yeHbndx16UXjYeTN8+Hgwd6N1sXGHbpppfWXkXZVYiU2nSTVAcDlgLxwlyh1XEWMH2f5/9tjsY+Fi2QfPKsdhvm+2Vq6Hp76g5pq6kgySZY+BjcKII4a+gkGGAYXuhi2LYouLjbiTvZg8nliiBqlrsmi3bMH0ylXVcNzd5dHwgPm1A9MKwBSQIMEo4jHCPKxCHkymVEFatl7yZnhqc2/6dJR4s3dPeVZ9hnvaeNR4CXeEc9pulmxfZOVhwlmHU1lOHkMNPAU0XyhzIpUXdgs3ASb5LPGx5grd99VTy0LE/rkZs0Gp5aUinmuYQJJAjVOLLod/iJKDqoN2gpSBp4buiCiOqo9sld6Yq58ipKStPLWSvXbHRM+F1tngI+sn9iv+CAcXEeQZtyNvLjw2hj6MSGFPMlYfX7FjHWiwbLxw3HbCeJ15z3zVe3l8RntAeAR0KXJTbgZqWGScXzVYE1BaSZ1BJTc3MW4l4R2CFT4IJv9L9gHtRORL2u3PgMZevS23K67hpxajrZtTlqWRpIy5h2KIG4fsgxaEo4TOh0CH6YjGjlCTJ5Xvn42jEalcr5S4O8BEyZ3S19lv5ILvTPn9A0oMpBZFIAspZC8LOmRDVkvbULRZ517rZadsg3BGdSB363jgeYN7FnsyfeV3nXbucXJv12yvZnZhMlzNUqxNB0cbPsQzUis5IUcYPBB/BaP6VPKv6EXc69RozU7DlLyHtD2ryaLDnymZrpI4jlmN5ohRiDeGkYQbhPuFXIY2irmLPJDUk2ycFqHtpQetZ7RIvJbFKMtA12fdgOoq8bT8ZgfQD0IWryUMLCoz7z8jRWVPP1YlXoFic2htbcpxCnXodw94ZnyUezZ9n3l3eEl1VnNUcJxocmaRX7hZnlD3SzFAWzttL40mTx8xFLwJS/+i9p3t8+Me2hTRecgvvj63FLC0rFWi+JkSl4eS84zjiS6J1oOthj+ESobkhsyJsol9jXiQhZZmnaih4KfKsAy4UMCByXHQN9n/5ZvtE/sqApgLiRV4Hu0nRzChOPVBSUgkUVZYPl3gYRpp2m4TcwR4LHrueLV84n6be+R4rXdFdXRyi23LZmdiOlwIV3dQLUSPPYgzhiyEI30Y0hGfBDP7zvIG6gfeMda2zafEKrzRsiqttKUcn9+YOJUgkIyJVYjIiUqGCITkhKaD+ofLhwKKE5Fck9uaT6Cuo9+rB7RwugrEhs2O1ezf4OXA8dP6GAfNDlMXGyPUKmo2bT33Q/VL91SIXCRhamgLbqlyt3PFdgB6Tn0xfEh8ZnqZeeR2dHKnb1ZpBmgWXq5bqFI+SXlDGjvwMOEoeR1xFiYMkwD490TvPORD2lvRxsmMwAm6rLALqJ6giZy7l3KUcIx7iuGF6oXKhXGFeoSQhQaKAInNjlySDJX/m0Gg+qnKrby367w5ybzQCtim4xfwJfkmAWsJjxRgHLgnrTE9Oe9BD0lRUi9XYV7WYnxq/GyrcHp0XnmredV+oXnleiF6InmFdAJxhGyLaF1kS13AV3RNukdqPxw3YC1TIrgZCRI3B6v9r/QP6fbf1NbezIfE9L1BttGux6R/ng2blJUcjmmMxYmPhm6Ev4NYh4CGkYUshyWMJI+PksCWVpzIpeGrj7G6u3jDCsqP0DHca+lC8Uv8WwaxDe8XPiI4LIg1xDu2RM1P8FMAWzBiN2bwaoNwY3OfeMB4K3oVe4h7T3ykdsd2fnWtbr5rIGYmYUpblFIeTTREDzv1Msonkx1IFjcMegOp+IvtQuVd3zLVCsrswwy6HrIeqj6k9p2el/CRyo70iaOHiYPtghaD04K2hjKICYnbjYWPJpcgmh6gHKc2r423Gr6gxivOEduw4a/qfPI9//0IQBIIHJ0kFC0BOZ9AtUYoUQ9Ws1zWZQxq327BcJ11rXgUeWp7onu4e7h4wHdrdPFz4my2a5dizF4fVnpQHkeTQA45wi5TIxgc+BGOCLf+LvXm61bhfdjY0F3G4b7YssusFaeZnoSblpRQj36MqonkhuyEeIQIhXSGAYZ9hqiKoYvClNSW2pzko6GqlLJXub3BB8m+0pnd4+ag7sL7XQSbDK0YyyF5KVE0sTpkQ8NMhVK2XI9foWYNbBpvR3LxdhV1Y3sZehR7WXkseZF1m3RbbkBsCmV6ZC5cuFW1SftELjzYMm8rmSIzGH0NQAI3/EjwgOdJ3dDUaMsjwna6brKgqiujbJ6cmHmTTJCSiYSIoIR5hVuFzYTTg+2FW4qKjnqQXZNFmXSfjqmgrzi3ub1LxibOVdcf4Y7sZPYm/t0HbRHLGm8lMjDUN9U+K0iITsBU4lxqY2RrBG4GcJZ0LHeUeBd9m3vKfLF53nl4eXVzyW0UajRjz13gWPxRPkYcQcI3QjB5KBgeXxJvCSoAifUd7MTiFdkj0lHG7b4BuGmwQaikpD+ZpZRwkXiKrohzhdmFQYZShryDaIVtiMKLyYwwkjKXXJ1Go1updrDKt2TA0slQ0QPbxOc97if6ewIrD6cXZh9UKZUxVjl6QiJL/lNTWwpi7WPsaixwMHOAdvt52XjVfEh8vHxrecF3kHQOc8lr3mZJYjtdvVRtTBxGiT10NBsruCHcGNoPvANH+svxv+Ws3UDUhcufxrO5HrPFrKKhTp+UmMqUu44GjOmHnIZzgzWEe4aBgk+GwYeDi+OQBJZ7mu2gEaYvrpi0Er/9w+fOaddm4Z3qhfRJ/KsIyhHWGr4kiSwuNbg+wUVvTqBVjVwPY7Nnx2twckZ2wHW0eIB5gHpKe5p7Hncdd0h09G0SbPJjrWEzWcpPiEiiQMU42S8cJ6AcERWQC18AFvbI603jaNp40TDIRr7Mt7yvBKlVoMabPZTUksGNKImGiCGH64RCgzGHqYRrhwyJ545cklCYdZwxoG2pgbHJulG/V8ih0h7aQ+Mb7Lv3iAE1C7ATdx8LKBgycDh+QgNMQFFKWfJfP2UiaqpvE3L7eNJ4bXslfTV8XX2de3l4/HT1btNsOGleYlZdCVZrTgtFHz81NtQpRiPYGkkPHAfE/TLw6ugG4PPUv8vJxR28XrReqoGkD6DPlx6Y1I/6ioeKVocdhXyF0oRwhdmGi4g9inyO0ZWnm9CclqTFrX20u7pdw+XMT9Wr3qDkRfFf+owDnA3TFw8iMiyDNKc+JUgYTtRT21uWY0tpDmolcbV0aXWsesZ7CnvuezV633k3eM9zHW/7adZkPGCMWJRUWUsMQec5cjLkKP0dcBUJCn8Alvh762HkVNr2zwHHCMEHtXqvaKoFooSaSZpFlAyOcItkiV6GAYWChGmCy4Yhh4uLjI3PkraTwZufopWnZa/Ktpa+Mcmr0BjbJuMA7oj24f8QDOkQjB/oJlYumzlWRBhLQlB7WXZfaWPAaR5u7XOkdy94Qnyme7p6a3uJelB44XWEcPFsJmb2YbhdelZzTdNG6T63NZIrGyN8GgAOYgY7/rfys+ns4F3YW8ynxQK+/LUjrk6mjZ/Ul12U34/Ui56HZ4X3hjqCM4RNhd6GGImljFuPDpIwmMWfuaNWqzy0KbmyxIHKKdQI34Dn6fPa+mYFEA46GDYjIS0pNWA+i0WrTwFV/loQYpppimufbjZ0ZHkVehB8f3q+eyt4iXsfeYh0O25IbsBmGF+6WIdTBUvLRHA5kjGkJ7oeuxQTC5gB4/g/72Tnsd061FjH/b9puCuwsatXohidkpU3lFOOL4uBh0CHCoWvhS+H0oXLhvuKs48EkXeWq5umoV6oR65WtdW/Gsdpz+nY4uMk6eL1iQDzCGUR9Rz8JjIvpzdWQFBKLVE+V9RdnmYUaT1tJXFadCd6xXtKezt8aXtieYR2/XQ8cM9u5mpgZIVdWlQfTWlIrj5PNrUuMCRmGaoRtAhc/V7yQ+pr4djWac7mxYm9obXRrpimCKOkm/+UKpCni3OH9oePhVOD5YQdhlmGvIczi/uNupJHmFedhqFRqxWyfbkWwqXKedPF3ajoG/Fm+X0DbQ0vGM4g9iaIMjA8DkRSStpSElrRXz1n8GvnbWV1NnYoeFZ6KXzeesF6EncDd9dyO3DabVxmg2GvW3VUWkt+RAI7PjMtKmkfDBrtDCkCFfyu8A3lcN0r05rLy8LZuSOyjqg4o4qfCpbHkLGNiovDhXiIlIX0hs6FHYX7iJmHHIzckCGWgJrfn72lO68YtVm+ZsWGzpTWk96i6XLzWADeCTUUIxyNJRgtbjcWQFxHPk7RVcdcQmXYa8Ju0XEWdzV3HHz3e5l703o3eq14D3duczFurGjhY6FdLlivTVRI/UDcN4kvqCSzG88Q8wf6/Zz1OunO4AHaks4gxx2+mLf+rjOqAqPFm5iWaI9vjm2Lnon2hJSGlIXKg9aG9IijibOQ95KGlwyfoqJLqXWvD7rnv4zKkdFL2kHlc/Di+HsDYQwwFVAg1ilYMSo7ykB4SztVCVkAYhBlnmn1cQZ0/XSSeJN6Uny8fFV8Gnnmdsl1AXGBazNmDWI4WuNSekoERpY+LjPLKU0ivheDDfYE0/qf8H3nNt6T0hbMNMCZu1azaqz4o5OaWZmtkzGP74yHhyyFE4VogYKFtoMchrOKPYs7kQ2VT5lIoD6mVq3DtDq9zsUwzozWXeDz6SPzwvxhB+EOixpzIj4vMDZMQGdFYE7bVUVcvWLBaHptynK/dpt493cke+F6i3rDeqZ5F3ZOc7RvKGmUYZReg1UIUppJwz9IOXowoyUOHtIUXwmS/9b1FuyX4VLWNNLZxkLA5La8sMumvKHrmCCUT5E0j9eI5Yekgx2Ei4YchFGHWYhciA6QvpLQlv2cf6UTqw2xJ7c4vy7IfdCg26rliu/r91EB4Qs3Fl4dTij6MHM43UXDSs9TnFuRXy1mmmnHcIN0WHZSeW56zX3Geh16RHn3d8lzcnIJbX1mGWLSW2ZU7U5DRfw7TDSzLGkkHRjtD3wGi/oa8fXmBN2/1eDMdMMDu1i01ayOpCKdHZiylVOPYYmJitKHn4V5glaEuobeg6+JEozXkZ+TSpnNnBKlXayotDO7UsP0zHLXzt5o6dfxXvt4BWkO5xjWJJorHTYfPu5HcU3wVahcDGGpZqxsk3Nhdql2m3iJfMt71XpteWV41nSOdERv+GkjZPJcJlgdUgBIUEI3OcgvQCfVH60UpAtRAnP2nu0B4w/aXdGVx0C+HbcIsn6ooaEenuWXXZOQjYiIr4cshhKF3oWXhNiF7IdoipiM/ZHXl7+a+6Hpp0qzPbbIwYvGNtC72VnjAu4B+LL/BAqjE9sfOSh4L4g3PUHLSRNSJ1ZiXiFmCGihbg10i3eheSZ8OnpnfCZ8DHvHeMx01nBkadpooGHfWfRVdUz0R9Y9rTUaLcwhLxq9D+0Eo/2B9c/qbeFq1crNJ8bvu1KyBqv3pjyeppr+k7GR9ouFifSGbYWChBKCH4R+hmKKVorckOeT+5r8ntyhxapis3a8GMQ8zNLV3t4M6r7xePkgAoEQABrKIaIsYzbFPjlFS03rVQlbYGDZZwttJnC8dO52LXqLehB7+3txejh5lHWMdGZv4GuqZGNeM1rKUYlJnEGKOw4ztCk0H8kUew2XA6H3Ae7k4yXZ+9I7yGvBqraWsF6pB6LsnZmYY5J0j2OLKoZMhq2EXYQ6huKGTYiwih+MkpHkk/ucDKD1pyKwJ7kjvoTJY9DE2Ivhf+yp9QoBgwhOE9QdJyZUL8o3Jj+ESKZP8FjcYKpi+2u+bRdzdnZNd5h7q30sept6i3ibd/R2+XK9a1FqSmQ8XuxWZU71RoA/7zf1Le8j3xmnEuQG6/3q84rrxeJi1+7OcsXsvKq3Nq1/p+KfjJuhlF2To434iIyIsIWeg1aFZIVLhnqH64o+j/WRoJqknp2i8azAsam5Ysavy+DT/t3e6JbvCPzvBEoPRxdYIFQrGzWHOiJGHE6cU9Nd2GK+ZtVprm9AdAZ4Q3p3epd7c3rOefd5HHkmczxxDWp3ZKdfAlojUwRLo0O5OzQylihKHzwWtglJBbv7gPEf5VfbqdP1ytHAEbcxtGCrxqIxndqWC5Lzj36LdYoSh4+CmoOFgZyFH4l+ilKO9pHUl5qclKF8p5qu2LSQvqbFEM0b2qzh/+uo9DQAzwjdEUUdLSdrLuI52D34R3tQjFWKXthiZGsFbM50q3ZDeGB6znvle5d8HXkDeU12f3JWbUVoYGQjXnxVPE+8RkRALDnuKzIkGxtcEskIs/3z8rXrMuGw1/rPJsYOwKu16a/xp5GhDps/lw2O0I48imiI5ITig0WE84I2hpKIKIsTj16ThZn6nMmjN6o7sSO7esJ6yQTT7tzp59rvG/lFBXEP8RXDInQocDPHO89G40o2U1ZYl2IuZqpvq3CDcl53W3kkezB6W3xJe719zXimco5yBGo5Z+9i51qRVaRMlUUZO7Ez6ylFIjsZeQ0YA8P5xe0a5RLc79KnzZXDXrjXsgyqmqQLneeXipKCjiONbYkWhw2FvoTEg06Fyojxio6O+4+wlLmb4qALqM6t3rY1vYrGccz01xPg7Onx9u0AZAnXEnEafSQUMJU2vD5eSHxPKlbTXdphEGj1b9RxeXV7d0h7XnzBfK15n3oTeNxzDXDzbypoa2MMXv9VtFIzST09lDirLhsoOhw7FC4K8wHH9pzt7eGs2FTQBse3wCu4t60Mp0iiWpmXloWRmI2BhzWHxYevhVCGD4QXhryH3IrIi72VAJipnJKiqqkXsi+60r8AyvTQttwk5U7wSvlWARELABYqHSAozDGyOsdCjEi0U+1Ynl7RZ6ZoSG8Bcyh2zHihfIJ7rnxCemh76Xg4dJ1vn23dZtBiFFwuVFFMv0bYOhIzDS68IUAZiwzSBE37lPAx6BnhMdPszsrGfbzssaaqpqNknKWaiJNekGuMc4cBh7+DKoTshBeGhIY4iQ2LrZC3lgmaSJ+9pXmtgLVUviPFqM1q1cTffOn+8hz97wa9EAYaWSOvKrQ1Ej/DRJhO/1SFXKVjOWlBb3BxFHTxeCl6qnrbfBd7MnrteCN3JXIRbuRqVWTsXzdZKVKMSRNAMTdOMcQmDx1nE5UKlf/e+V/uS+Me2/jPsskWwcm22LAAqsmigZyclSuSfY1RituHFIYWhIKF/4QchyiHeotUjtmPAJhlmg+ihKnisPS4qMFdyGrS/NoE4zrvMfaJARUNJhjMHYQq3zArOpVC+Uh9URVaKF3CZQBqJHBtdXF44Hjree14KXtoenp6bnjrcxdx4WtOaLphnls7VGZO1EV4PR40ACyJIk4afRB6BYP9dvQs6FrfVtb7zbXFb7y4s1SsmqNxoAuaDpQIj1+LtYhgh6mGwYTag6GGp4Tnh7uLfJG6lWWZ15+7pResbbK1vSPFJ85b1hjecOhJ8r38pgRFEOcUEiOELAo2OD9PRRpPZlfJWeVhxWYBbGJwInQGdpl5G3vNfex4eXrjd013GXPKbeVq8WXHXQ1bLFPPSXpD+TlFMsQm4h+jFcII2gK4+LDthuSi2ybTU8i6wRS31rBQqFCiXZyKlQ+TlI0ti76G0IamhrqEJIdAhXyHO4igjdWR0pc/m/Ghi6bTr4i4pL92yJbRudk14z/to/c9/9IK5BROH4QmqTB9OXRBiEoZUbhaWWAgZONql20Vcih2DnugeGV7n3oZe7B3u3hpdP5yeGxbaZtkGlw7VrFP/0jUP0A3hi43JOsabREvBgj86fEo6bLgwdb3zaTFXb0ptIateqZ+nlaY55RZkAiNEoi8hzKFx4Pqhv2EGohsiHyMU5EGknGYD544pMqpjbSIuZbBlsvh12jdO+bc7y/8uwYVDn0XaCKuK480vj6pQVhMlVfDXEljoGZAbdtwjHEdeCd6QnpkfXF8yXjJeOt3KHHlbiBsnmXVYm5ZXlOXS8BEEzrLMLgpcyAQFscLPwQH++7w2uVU23zT8ce4v2S2WK+AqTKjK53elx+TqY4kjGOJu4Y0hJqFN4NShsaHzYdQjYKQy5W8mm6hKqcQrO+22r7pyEXRgNf64vHrXfZg/wkHuxR+HEMlAS9AOWc+MkmSUIpV514aYbVpO27Jcpt1Y3jQeaF7NXu7e9p6hnq0c9JwxG4uaMJhEFqdVV9ROUhJPwc3Ei51I50aSA/7BgT9QvSQ63DgPdmJzYfEl73UtfitKqfAoRCZUpaOjtiMoYtViHWGcYNQg/uDk4QYiaKL0o7BlYSZip1EowOrSLJvuObDQseR0yjdmugA8df5xQC7DgIVUSHAKP0z4DvKQ5pML1XuWlpiW2Z/a4pwaHOCd8Z69nnpe2t8GXl0egZ3lXNzciZsimXQYeBbSlRLTQRD9D7bNGUrRR9FGLcMyQPd+t/vnub13D3Uf8zhw2y65q9ZrGmiAp+6lpiRF484ikCGcYYoh5aErIOrgqOHX4k7jE+R/5bJmRKgJKVWrry2WL5VxsXOftav4tTqjfEl/L8IdRBRG1Uk3y9vNy9AREV/TlZVpl+xY/RqSWwgcbV01Hg4em99fHzse0t3HnjHdUVx/mxdaptktV+RVt9RrkmvQGU24DEBJJEaSBSACPH8WvTY61zi69Vh0d7Hpr2ktievI6hLoKCaAZaVjgKMMIpKh+GH94XlgkiFToY/iWKKAo2ilCuahJqPo6erJLMNuZfByssW0BLeBOX/7gv4swIeDMoYiCADKPoxxTtDQqBKTFO0Wl1eNGbCbLdtFHOjdHN5Cnl8ehB8TnkZe7x1Y3SscIpql2jhYfpabVMzTb5FcD2rM1IpvyMrGaAN8wMZ/B/xEOr33qTUOM3rwie8D7Eoq3mlk6A+mviTXY7SiuSFAYaIg0iDR4SJhFqIqocbi+COLZYOnAWgFqYjrR60uLtnxFbNzNVH4WfphfVM/UsIZxHzG/EiqyoaNao+cEX5TthWOluiX49p92ubc2VyNHgWezZ6vXmRezl4xHc7d4lxzm03aztlJWB7XOFP0EoHQxI6ejE+KIseaBNaCUYA3vS47BHh/9kD0HnIQ78ztsWu+qW4oNya2JPvkV6M1omYh8SFBYWdhQuENof4iH6NJJHAk6aWB5s0osipFbAkuQjAg8qz0Bvbx+SE77z5sQHEC2YV6SDuKKExkzqPQzZMQlNBV6xe2mXaat5wUnIPdd56O3q+fD19hHqkegF4TXWecAttZmbjYHVZp1fnTUhGwjzcNPcstSI1GEER4wYi+uzwr+nB3mvWNc3xw766obMDrNul1J8emKWTJI0ijsGJCofrhRuEJYYBh0+I6YkMilSRwZTwl7SgpqfFrVqyt7oCw8TMyNjo4ALqi/Bx/SgIYxEiHCUkaiykNtg+pUZbTgFW4V0fYopqc2tLcB90GXq9eW15Pnwxeb56M3ktdAR00W/6aollz15WV+dSG0mLP6c5DjE+JycesxM7DLMB8vel7vrjJdwU0o/IRr+pt8KvD6qYoNqcoZWmk3GPjIlgh7aFu4J5guGF64b3hSCJ14yfkmKVHJzQoEynSK+7uCvALsp+0SDbRuL37dv1QABjCpkUYx2MJXEuvji/QZ5Nfk8qWPpgO2O4alRw8HGRdE96y3uZejN9lHnjeD13z3WFbyRtx2k5YgRbrlW1TY5J/T7yNQMuZSIDGkMRGQdc/ojxjee24NXVuM4Pxku9B7R6rn2nZ55dmeKUAY8JjGqLgYcBhOWCwYWhhiqGRojpiSaS9ZKql+ygm6WvrBa0RrrJwLbLt9U03svoPPA//S8G6w7mGB0jKSpwNd8+UkSSSxlWsVmsYb1ohW7xb8p0HXmfez97GHqRe8Z5rHo0dnJ2EHCvaf1mUV8wWsNShEr5QkU40zKJKYAe9RdMDPYBs/nj7Ijm8t200ivKe75guSaxLanYpAmdm5fHj3iN84jShg2G04UJhG2DFIiXiHOKBozbkF6W6JmooPimaq/9tYPDZ8jIz2zW1OC46471+f1nCRcUix1KJEIvPzmGQIpHglD+V/Zde2Oka/JvbXIDdhV4rXqievR7u3zXeiF3NnK8cH9tOGp3Y05gRFeITuNG/j0RNr4r7iPbGAsPcwYNAHj1xesm4tXZTs+Ixji9a7VFrdClFZ5SmtKTKJDCjOiLa4gJhQCF84Nih4SG2oewjcmP1pRlmAOcLqULrPOxP7oMwxLM5NW13oTn9fAS+a0CEQ/FGH8hSycoNKg9fEbCSyBTjViAY1dm6WsOcrJ0EHiMezR6in2Be6d6THmqeE1zOXHrasxld2E7WWJUSk1TQ7s7rzBaKXwe+xabDlUCc/kF8aXlttwO0xbKnb/suLyz1KpdpE6bSpnBkXCO34yui42E8YSzhd2EOYU7hfCKqIzUk+6Tu5hrot6m8q76t669o8cXzsHZ8OHq6nD1a/55CGITwB2kJN4uIjiNPjtKIU/xVtRd32T3bKNta3NHdrp4g3qqe6N8znvUe4F2CnYTdAJtRmbyZAJd7lVFTwFJLUFpNeUu/CYmH/YR7wgbAMv1o+ub4ZHYHc9txga+rbVcr2iob6RsmnmUOY/biXmJe4cbhl6DE4IJhUyFo4gMjYmOYpMOl3ufRqJNq2KzQrgGweLJv9P63CLpCPCY+n4C+AupFrIfAymSMcw5SUM9SkBT8ltLXxJlnmrnbcx1XXizecF733gxfOp5O3l7eGtzpXDXb8Fmhl+/WpJTpkwIQz899zIkK6AhvBfJDQ8EiPl08TDnx9+A1PvKO8F1urqzDa61pJ6eVJifk4KPbYwWiZ6HNIVahRuENoV1h3WI944jkR+TT5nIoFqnV6xFtBC+7Mf7z9TYYeAC7FnzHQAZCagR/Rv1JjYtAzbOP0JI7E0gVVdcaWVTaapttnBzdZd1OXtGez16qnr8ehN3YHdzcXRvdGmUZjVfmVc/UcJLZEJ9N+8tOSfZHDQVxgai/2/yqe1k4+vZns4Ox7O9O7eYsOGpL6DGm6+UH5JVjMGKhobRhUqDEIT4gzyGyobVihOO8Y8Tl8WeCKQFqCmvxrsKwd/JFtHw2sbjPe1J+W0BOA2gE9wdXyjpMm86uEEcS/lSIFu8XpRmnWrycHJyrHYweAt6ynplfcR7KnlqeGl2EHJDbcNn8WJVXaBVbUwuRfU7WzRGK7ghBBqiDwcGMvtY8Zznc9251MLL7sF+vP20rqpqpRWef5dKk7qNpYwCieaDg4fyg6KE3IQwhvmIVYwmkaiUmJnqoCKmiqshtQG7tMSczJ/Y2d3i6PXx5v5rBvgP8BsbJm0tfzQUPvpHAU8tVJdfEWORaeBrBHHudVJ6enoAfDl82Hzxee55QXZQcU1t62s9ZcheyVl0UsFKQEAfORAwTCahHJMTjAltAWv2U+xZ5aXaqdEcyFrAQ7qprzKmYKEemqeVp5DkjbiIGYdLhz+CpoURhTeEjIdRi5WNtpFFlfWb66JYqyawRLdFwW/H/89R2iTlhewT+WgB9QkMFNQdgid8LiE7UEBoSuRPh1nHXTpk0GpTboxz1Xb5diN6MXvjfGB7inugeXZ2PnLzavRm+mAvXVJXTk57RKpAHjaZLocktRheDdQDdfyD85roD+Bg12LMh8UIvdWz6KoCpv2eRptxlc2O1YywiRaFloMchE2GEoYRiGmKkIw9j3SU9ph6oMmiM6umtOO7DMXRz+3VBODY567xxfxTBS8O5heuIwAsFTbJPQdGQ0umVb9cRmFqZ11sIXFhcnB4inckexx613vaeiN3K3e3cc5xMGtfZv5fHVrgUftJ10FwORgxLym9Hr4VyAoMAC32B+/k5AzcOtPIyVPBkrrjr3qpM6OEnKGVQZO3jqiKMYfZhkaF9YPCgn6DVIi1i7eP1JOblieZ+6AiqLGsw7UqwDLHo9DG2dDiGepL9wAAxwiqFIQbCSfXL7g39UF+RhxQj1dEXRRlbGr2bUNwknY/edJ5uXoLfLh5THrqdDxzZnMGbNpnnmBeXNFVtk6jR4o+RTYJLmwkXhtfEBYIgvyT823qcuCm1xbOMcNsvqCy1ashpmyeMpr9k2iO7osBiPyHxoUoggiFSoVYhjmJSYo/ka6RT5jinB+ndau4spa7ssMLy5PWi99J5R7vkftUBEIPxxaaIZEobTLiPMxECUz3VWpbuGKnZoFvTXHgcz93eHrLerN4Bnw7ewd5NXflc+xsPmobZt5hUFpLUr1LckMVO8cx/ip+H78WGA2nA4z55++p5Xzc3tI5yba/3bhOsjGp+qN9nFKYH5O+jZ2LW4kJiIWE8IOhhVCFy4b8hpiLx4+emAadlaHYqNOuXrZFvyPLw88D21PhGuzz9q7+XglyErAcFidWLvw3wj6SRxhQmlaZXqtiu2Zxb4FynXY2d1B9mntre0p60Xpievp083FMbRJqt2N/XaZWB1BtSI1BhjfbLXglkxxCErgIh/+B81fs2t/32DXO9cc3vkO3a7BAqKSfLJ0elNOR/Y1QjJ6HJ4T5g9uDp4UShQOHs4vVjfuSYJdAnr2lWKufs3W46cBvyRrWBNzT5qbwEPqYAowNaheOIC4rnDJtOrRDWEyFUpdaaWKeZ11t8W+LdNZ3wXeUe+Z733owf8957nbucyFuh2zKZ85gglt/VBlL+0NCOmEyOCfOHy8WLQw3Bcr65++a5XHfXNMLywTCMbqlsmCp7aIsnY+ZfZHtjZ2LpoYkhwSGFIXfhEaG7YeAipWM1pKlk0+YC6Dnp/Gt37c2vfXGA8/M13XiTOoY9pr9oAjaEZ8ZxyWPK6s20UCCStZQdVfuXAxi8WoKb5dxjnbfeE968np/fHZ66HqFeIN1ZHEXcG5oy2SiXl9ZmlKrSbk/BjmXLecm1Bo+E+gHPf7I9bPs0+Pf15fPjcYIvza2G65Wpo+f1JsvloOPJo3Ph22IU4VThbmDv4VRhm6F64nXjgyTApZnnE2jSqpjsVm47cGWyf/TJ93Y5NzuVPmtASwNmhSQIT8qHzOuPPNDwkvtUhFabWCdY0lr624Ode92qHnNfNR6U3vHetJ4RHUedI9v9WtxZtJirFuyUpNODUSQPqU0OCoRIo4YiwxBB3b6z/Eo6Azek9W0y6rDi7ymsTur26MYnoyaQJQkjxyNMocIhaCGTIYFhm+GzYfWiDuPB46vlEyaMKDYptWsC7SBvTXEYcxz2AHhyuhD8dX9+AgxDv4Z4yV7LWE22T88RxJPnlbsW3xibGfCaxRw/3ReeCN6lnwMfNB7Z3preWd2knNxbDFqu2ZCXQFZe1C3Sy1AqzeyL6AnFh5cEwwMJwA89TTsPeMt2VbPVMfrway1qKw9p9Wj/ZsUlReRGI0JjPeIJod0gsqDUoQMhYyIGon1jlqTrZXrmi+jqaiLsvm5Dr8yyTfSAttO5O3s4/f9AWUMahOHHsEoZDA6OSJEakqBUpdYql53Y2tpCXJ4chZ2CnvYegh9Yno1eqt6AXpMddBvFWx6ZxBiDVwgVYhOeEZSPgo0Yy2rIhEZIA5mBQv9evFI6Zzf+dQwzIvDFLuysu6rB6drntaYlZG/jaSK84gQh7CFyINuglqEboYFisuJEpF+kxCZ255npiKufrLZvLTCTczr1mDelepi9O37KAWGEOUZNCOoLCg4nz4pRhFNn1SrW/Bh3GUYbiNyzHP0eNh6r3uve859NnqAeHx17nOHbaJqW2XvW5xZYVG9SIdCKDsuMfwmMh7VFiwK3gD99hjuU+N/2UrSSshJwPi2HK9yp46koZy2lQuRZ47tikiIiIcUhbiEf4Rxh0GGF4mjjoSRcpb5mdKhGakLskS3075SycDRHdz65OvvMvWcAQsKwhOtHmonGTLkOAVDnUogUzFZc193ZB9r+m3ncjN3mHjGe217fX0yfIR5WHdZdMtwjW2yZ7Rhv15BVetOAEeEPsc0wiuOI5EZww/ZB0H88PN06dTfH9bezZbDRrwytqWsiKdjn2+YlpRtkQyN5YnThVeCO4Yeg1GGAIiviNSMSI9VkvWYy51IpN6pTLIUvEbCrs3316ze7ukw8on6CwWfDcgX2iI0LBk2/T0oRTJMNlaDW2hiiWlDbqVwGXP6dxN5eXplfI18MHuYebx3m3M4b11rUmRIX89b+1HVSzZCcDprMT8n7R2pFXIMxQJt+PTu8uPf2rHRz8n1v5S2urElqdShb5xulwiTMY4UiiGJj4RRgm2F3YTchT2HEYozjCKQQ5ZmnFahr6QqrRi23r2Oxo3P4dnt4VvsPvcZAIsKpBOKGjAm9y/oOIVAa0d4T8xVxV++ZDlpyG78c2R1G3k9e8R91nnBel14zXTIdFhwV26QagVjQ12oV8tQEUbhPpY4TC8GJ1YapQ86CU7+b/ht6KnhVdfXzU/FP7wytbStj6Yjn7uZ1JSxkLyMWIifhXKDPoa3g++Bc4TqhhmMRI5qkZyXjp7ko5mrtbEgu0fE0M250wDhHOTN8VH8AAJdC6UZRiJ1KaYw/zvCRJpLLVOKWy1j4mUlbKdwpXOEd4Z5l3ppfdN8E3t0egZ4IHSxbzxse2fyYDFaylO5TCZD2TyRMY4pgx+OFREMYgGw+QPumOSN3fTUx8uawUa8NLJQqUmkrpwHlraRVo7JiyiJ94QPheeDG4QMhQeG8okSjRCS2ZXhmG+hNam1reO3wb8nxUXNBdcQ4yzrk/fs/ncI2BFhG1YkMyyJOFhBo0crTrVUnVwaZgZpvG7mcutzQ3dLe4B5uXytfC169Ho3dAJzbG7iZsxjbFwyVhhRKUbcPyc33S8GJusb0RO7B4n/4fUo7DXjI9jLzwvIP7ydtc+t56cAoZCalpdCjqOLfIl3h4KHq4Zbg/KDLoR9itmL6oz9kMeVPp0uo3GrzrDTuHjBSso/0y/cAub77lX6RQLMDfwWNh92KSU2BTt5QzlOWFSQV1xhFWZHbE5yOHKwdyl7bHvwfER8KXm0eAV4iHIYbwhqyGY7Y0ZYs1VgTHRGCDwXNdMonR9ZF8gOMQPF+iHzR+eb3+rXvMvhwHS707Rsq2CmqJ6MmZyT0JBwizeIL4jAhrqGhISWgj6GeIrvi9aRpZXsmlehuqdxrbW23b0exqXPSdev41br5/Na/XoJPRJrGcoksCt3NuQ+OUafT29UvVxlX7hoM20gcuRzxHd0etB6Snu7eud7R3q/dFtygm3bacZiv16UVg1R+0e2Qss3oC+DJksceRK3Cdj+zPVc6+rimtcQz8vGucCftRevUKi/oymbHZaJkAWNuopQiAWGloS1hemEsYQBh2GKuY7fkjqVi54doXWoz7HVtrLBdsls093b+Oji7R/65gLxC9EWhCCRKbIxvDp0RFVMyVNZWrBg7WWFarlvg3M/cvd5T3vnenZ7uHvFen94PHW5cIVr/2jgYQVc7lYzTZxFHD1DM68sjyNXG6sNGQa7+2HwLehj3hfY9Mx+w0S7O7XQqyelcp5ImS6T/45jjEmHUoXshD2E+YI2h2KGQYiKjDCQzZOXmBGhgqWkrmmzHrz2xDnMcNZA4GrrFvRI/UcFwxASGmUkFixVNt88SkbTTiJWh1weYBhopm0Vb350snhjeox7FX11fdZ5UXmAd7h0p28KavFjDl7lV69RE0jDQS86AjD1J/gbfRRQDMEBL/V96y7kMdh/z/nF7r9stiqw/KiRojybP5bmkNOMiopihDKHkoHfgheEwoKniEyKGI8PkrSYMp7CoeapTK7Itua+XsfKz1zb3eKL7lX2pQPtCasV1iBnKI8wPjpTRHpJllEqV3BfrmJma0lvpHQwduV5FXseexB9vXkbeDR48nOvcN9sQGgxY25cGVTRS9lFejwwNdQsZCQhGgcRXwaJ+23z3emK3q7VfsrKw2m+LrOMrlil1KBrmkmUhpBOjc2JNIaXhZWERoQCh9CG5IgrjO2PjJYzmGqcuKUGrOW06bqww2PMg9WM3k3o6PRP/CYFMRB7GR4hjywmM1E9akWJTmxWw1y7YRZnimyhb2xzt3Zqeqt6FHuYfOZ7rXh/dbtxoXHMadJmR2BmWvtPzUudQEQ53C+iJ0ggAxgDDUwAFfnC68Ti1drG0qLImL9BuGSxUai4odKdMZYDkT2OyopNi9eEyoRBg1eDXoYSiCyIVo7RkeiXN5tzoG2odLEstb+/Bsbg0IzbnuIS7dz1qf/BCOMTdRz+J54w0ToyQeRIx0/JV3lf9WIqalZvzXBMdSV5MnoRfIt9IXvYeqJ5W3S8cTluR2aQYypd+lR+TqJHaTxTN54tcCQMGvMOTggi/tbyIevy4MXWx8zYxqi8Bra2rGylrp+ImsOTs4/yjOOIToe7ho2F7oSAhCCIOYcRi5+MuJIqmbueTKWArDCyuLuowYDL9NKP3n/n6+7L+f8E5A4zGRIlpStoM6A9p0QETIlSe1x6YgVoumzybrd1hHjDePZ7+nnxep93kXpWd6N1LG/eaoNlAWINWnBRIkzzQWA5STGiKXkg2BZFCokENvgh79nnh9ue1LHJyMFGuNewtqmypEueNZd9kI2NuYuaie6GQIW3gcuEDYm7hlqInYyAkRqWuJkeoTamd7CDuJe+R8cez0zakOGm6gr1sf6GCKgTNB62Jr0v2zhCQVpIBFDpVrheT2SKa0FvnXIMd7R2b3rVePF66Xm5eWl5T3NdcxFurWqLY8Rd3FeDTqdI2j8XNoksaSX4G0wSdwlu/pjyZeoX4o/Ygs8Exhy84LR6rsioQJ9tmCaUBpAljOCKiIZ+hQmFp4N/hOiFyogCiDKP4ZQRmAaepqRCqTOzmbuews/J4tT03PXmdO6e+zsCnwsyFcoflihoMzU7cUd+S+NRVVlDYHRnQGs5cWJ2RXW9epd8x3t1eZR5/3fCdg902G8ba0Zlq2GSWWBUkExaRQM7BzN9KdIgnRZGDKIB/PqN7sTn7N321APK6cLEur6xlqj4onWcSpdqldON6ItcinOFS4RihfaF2oVuhtuIBowfkaaVwpwYo92lqq1htaS6dMUDztXXAOIU7Orxrf3oBloSWRvlJawuyTX+QONHyk6gWRRdkGP7aGhsA3ECd7x4s3iFej58IntoeSp6dnURcvJsf2iNY9Vc0FsKT8BIJUDyNWcucyP1G1sSZAqy/3r3UOwo4iXWutC/w2e+vbMuriGpGaF0mOCWcpLFi0uKZocMheSE8oVyhgyGsYd5ivaO0ZRLlmyd86ElrCSwSrrZwazJrtP323no1+4i+ZsCmw4IFeYfTCjZMKY7gEO0SaNTX1z4YX1lw2vRcRt0R3edeW15sXjAev16x3i3dlh0/3GObF1mD2ELXA9UvUweRuA8tTICKzEjoxcPDMoDv/tu8BDmq91a0/7NeMGUujiyYatdqA2gJ5hJlI+PKY5/ir2FWoRmhOuFCodqhxeIyo8zkICWF5uon1yn8q1ztLy5GsXpzADZv+Hv6J/0Wf3iBjMSsRg2JfwqEjWgPo5HKFC4VnRdX2VHaGRve3KZdJ53tnkue8t753qUeBB5TnV+cuht0myeZWtfUVn/ULJIGUH/OIYv8yRAHLgUfQrHAAr2Ge0U5Dna2NCMydS+TreDrz2oM6Enm9GV7ZAZjsyJjIchhguF3YV9hlaG0IYuirKPcJMmlzCaCKPVp2qwY7eZwRbKcNIq3G3l0eyU+HwClQtyFCgeaSl8MkY7tUCZS1BSjljkYVJlbGozbv1yvHdjeVN62XwAfQB6s3qXdv90n3FzbilnBGNxXC9UjUwcRWg+ajQoLEIjABmbDgIHyv6Z8ern/N8y1kvMF8SUuuSxOq0QplmdxpftkzqQFYy+idaHToTzhHGDXoTEh6OK94o7kFyUJJkToM6k/arlsla/L8TWzdLVL9/l6NXvFP1CBd0PkxxJI3Ys2DXsPOJFAU1lU0Ja1GAHaRJrsXCudBh4R3mPexJ7WnnWeON0XnZ9c3Vv1GtUZptfUlrJUllKPEGpO30w7Sc4HpAVAwyEAaL3cu7Y42bZ89FOyN7AGbfTsLyo9KILmrOVJJPjjQKKmIeuhWqEeIIFhfKF5IdOjDOMyZEklyadUqJeqLavFrlOwJLHh9Ml2ufiHO44+PcAOgxWFsMdKCTOMZI3lEKGR1pSPlhaXpNlImsWcANyr3eUeH56On0reQZ9ynz8dgt212/YbExoQWNpXUVV1017Rm4+2DRLLfUiihl0EfQFZv6M8iPqEeFs1jTPlsONvE2zJ609p92gz5mQlC+Pzomvil6IYYQFhMaEXoa+hQuI5osKjqeTcZi/n6qlma0DtES79cTFy8zShd4n6I3xxfyNCGEO8hZdIrcrDzRWPBRGrkuBVbZdV2I/Z2RrCHA3dI92OnrjeXB7x3sBfP95lHh8cmBvYGsVZYFfZ1lTUx1Lu0GkPOAwlChVIAQXwws1ASP6u+5d5BPYuNDwx5zClLjQsuCnVqJCnbWXSo+ejGCLnYivhueEb4OlhiCGV4i4iOGLbZJ2l+ea9aF6qLCw5rLpv7zHG9Ep2bTjX+uX9uH+WAlIE9MbRSeuMRw5YT+HR3NRm1dQXYdgUGpHb6JxXXcMea16enyNedh7PnsBeT51e3KfboFp6mOjXPdWlk/tRx4+eDauLA0jBBxKEo4HOP6s89XpNeKw16/Nd8fQvd+za65npE+eHpoflQCRE46yiCGHD4WYg7uDxoVvh+uIZIwCj4mSSJWbnIKljKkTs9e6b8IJy8TQbN4454TvW/jUAJIOShduIeoqsDVCPIxFmktuUjBbqmKIZb9soHK9drB2XXlWeeZ67XpOeoB4M3hodb1unGtYZVxhzlkaU5xLgkJ0OsYxlChqHl0UZQyUBNP5UfB35XfeT9Jiy0jD17mHsISr9aEfnvSWoZIvjnWKtYd4hE+HTIPMhYiGvYe5iT+NXo+xlOyZKKJGplWvFLi2vY3FG9Do1ynhZ+5/82H9MwghEicenCJLLws4pEAQRpFRh1V3XL1jlGk1bSZyq3Mkd5d6X3wLepl7uXppdtx4HnIlcDdsCmGcXZNYhk7zR2dC/jbRLXUmJRtyEtUHp/+r8wLs1OAo2bPSSMcuvNu2na/0pQ6hnZlwl++PSo6whleIRIbIgY2EcIP7hsSIT4qqjy6Ug5gJnTikRarZshG5icJtyU3Uxdsi5w3wZ/mrAqkObhT5IH4rYzOAO19EsUwsUCpbNmDNZRBrQHDTdLF2X3Y1e5F6k3r2e9B3oXbac8Fv8m14Z3BhMFhjVBhNUEaOPfQ0AisMIU0Y5g0bAz38CO/K59ndKdWoynvD0rkJsoCrvKQVnfyZapHJjbeK0IinhQOGnoM3ht2GYYUMiUeN5I/3ltya1J8Vp7Otx7TiulLFmcwn2GbhG+qp86D89wjrEKYYoCT3LJM32z+RRbZOeVcUXsJkS2ggb8hx4HXYeAp8uHvHevx4d3gLeQR3K3Hyb69pUGY6XdZYSFLxSMJD6zf+LegkBh0EE5EINwH/877sReQv2YDQB8j+voq2Sq2+qDWfiZ3qlkKSQ47ri/OG+IUXheuE14U8hJWKHIvTjlqSWZa8nUWjB6iIsSW4XcLfySrQOtwD54LusPjSAE8K7hS/HU4o/DKVO6xCl0oUVVRZC12EZSNqYXCscot2vnkvfBZ8X3xBfC57MXlVdH5xtmt/aSpgxV00VfhNyUWSOxY4/Su7Id0azw07BWz8vPJD6cjfs9evzALF5bsvtDeriaSKngib1pE5jyuKzIVAh4KE+4S2g4GFnoW6iOaJ042/lDGaOJ7/pUetNbUWv9nE7cxx1sTeO+rj81X8/ga/DrsYfiPoLjo1LT6tR8tOwFUoWvNi12d5bvNwHHhDecN6XHlwfNx35nqQd2N2QnTca7Vrb2QnXzdbi08LSdBDPjjBLF8nhB3TEmQL8v/S9T3uX+S02oLR58ghwHm3D7AZqSWjfpvll4+S1o5qiSSJUoT7hqCFM4RihRKILIlCj3SSc5UVmzWjl6p6rma3nb/hyifSH9tj5ILt1fhN/90LUxI4H1MnPS+0OBtC60giU0JZt14bZh1sQ20ock12Z3hKe9983nsEehJ4nHcKdkpyvW3bZ25jgVvIUQROMUj7PZUz3ipZIzMabRAaBrf6jfKJ6hnfxdVFzUvFy7kntOSra6YAoYOXIJRQj3WONIslg1KGTIOQhgyG34QBiBeMVZBgko6XHqDxpImqybIDuwLEmcyN1A3c8uXi8VX+2QRZEb4XCCJaLC80XT7FRrdPP1RyWzVh9meOahNyOXPaduR6PntYe0V8sHi6eX1143Ueb6Br5GV2XSpcSVInTK9CRjp3M98ogR4LFlUKmQE9+KntT+TA25zS/scOwi64brB5qSOk15xwlZ+RSI2Mi2CIQYdXhPSEeIfzgi6JzIpMjpiRmpXxnKujB6qfrrm3lb16x9/Pldln4j/tg/QhAeQGRBKrH1wnBDCROJxCYklmUk1Za14GZd9p3mxNcYh2zXY1ezR7m3t4egt4MXhSdftz7GsFZsRiM19lVmhMIEUDQDw26y2aJLYb2g/jBvz6rPMc6N7gJ9hVzzfDWbzztvCvO6dpnwqYfZaYkOeM4IjSh+iGNoXZg+CBtIaXhqKLXo7HktmYNJ56pCysK7LnurvDessQ1Are1eYN8V767AOLDjgZfCEwKxg0TTyaRBVOZ1RmWbxhF2cha3Zvj3UzeVN4aXq+fHh8fnp8eoR4KXVLbodsFmjgXnJbxlDHTHxBUToZNWgnfB5LFSQM5gNs+Cnv6OXY3MHSksmEwfa34rGsqhmiDZ0zmY+StI+Wiw+HEoaphLWFWYN8h9yIbYjdjl+Q0pXcm8ygvKhyrxe2D72/x6XPdNjS4hLsjPbW/6YJVxNzHYYmoi06N9tAMUkWTydWD19uZKRnv29ycJ5193gBejR6WXqnfNZ3E3chdSxwRm4ga1VkwF1OWDtQJUiTPrY0kS/ZJPwbXxH9B939dfVc66HgyNhlz2/FYL57treukaj8n8San5TBkyGO/YomhzKEFIXZhbiFcYSriGGMqY5CkryYMZ64oT6sbLEKuVbCvsxd0e/cyeaV8Hn9lwSGDjMWNiGlKiIzyjqyQR5NmlMoXEhhU2gNbEJxbHXzeXV69npofCR8WHuTd89yQ3P1b0huMGg6X85a8lFuTa5D5DsHNJUqWx8CF+0NhQOL++3xy+de3P7UpcxJwfG4lrFhq9OiSZ/5ma+T7Y75iY+HpITQhkiHn4M2hd2FaYuHjCiPk5Qjmnugc6YuruWzdb3ExJvO6tdX4CrrTvVi/mwHrBFXHPAkcywdNUY+Xki9TQRWf1zYYpJqoWwkcUx1hHefe8J673uSe593G3pkdXVxyW+caYFm1l3NVqtQjEiyQF44hC8qKE4dYhPVCSX/wPW36xvifNZk0QPFNL4/tXiv+qfgoe6Z0ZX6kOeLjoqPh2iFW4QShhOEW4d7iHqJHJDdkTOZA51UoXSqCbPuuXbA4Mkt0oHceub17574kwK9DXkVaB4pKYsxUTqSQdBKvFH0WcNhCWa/axhuUHP3ddN293uAegR7bnoueaF4IXXpbxJsymQXYlVbBVWXTe5DpT1fMn4raCFqGOEOQwVf+tHzSuqh377UAssWw/G7PLLKqw+ky50ymlaSjo9PjZeKXIXnhZKEsoIghuiF+Ir6i3iRb5Icm4ehwqXUrwi2Mb4KxsbOu9f14Hrpl/P0/LcFeRA3F7kjeiqkNvo+G0cjUMlW0ltJYhpoZ20+cfJ1vXbOeNl5Invfe1R6Y3godJJyCG+vbFhlPF+uVspO2UloQEc3aC+fJwce/hPYCyP+a/Vh7rThJ9ue0eLGzr89tlevZ6nxoQaaj5SfkXeM+Ip1iKqEA4hEhPqEU4V4hj+Lb40gk0WZ85rLoQCq1q6duN+/Z8q90v3c+OU/7PT4bf+xCWEUnR7oJ4kubjrqQLFJbVMdWZ1gwGhWbHltKnTqdfl4+3vEe0h813ogejZ3EXYVbvVtWWmhX2FboVXyThhGf0AUNDEsnCQUGBQPxQfw+pnwnem43SHVhc1vxGi+prK8q4WlwpyXmvCUSI8dizWLQIjfhYaFVIQLhKmF1InIi8mPpZIwlz+gx6Zcrj210rojxFHLt9cp4RjoofH0+zIGjBCiGDIiNCuFN4s9H0a5TnpZXlp9YsxntW1NcOd2lHgDemp7gnznfLl6+XckeLF0fXBgaXlltGBFWCBTykYyQTE5xDEfKd0d4hMADCIEZvZ57QnkV9uA0nDI7sANuCexlqoRo1eec5ZHkqmNSYukilGEE4eignmDvIMLiN+KPY2fkSqYpZteoq+n0q+5t8W/XssD0gHbxuKe7AX0If40CWkTlR5+Jeox8DdPQT9Kh1HeV4pdfWWgaldtBnJUd114KHlnfcZ5Knl4eIF2PXT0clJuFWeCY2FbBVXqTC5HbDzENiEtIyfMG18Qvgen/hz18efH34DXXs1WxL+79bSBrZGnnqBlmDKTwo9ujXyJwIc/hW+GIYbWhA+IAokZjXyOF5XtmE6dIaborUO01bukww3LetQd3Ujmz+8h/NEDbA5pGhskeiq+NUE+UkSTTo1RjFrtYUtqtmuQcIZ23ngQelN9JnuyewF5fHlQdmxzi2+zam5mnl/JWEFS9UuFQv86GDImK9gfdxU3DAYAZ/gG71bkatv00QTJxsJtuOmw3KhLo2ydDphGkouOmYpFh/eEjIU5g3eEV4VWiTOLn40jkUSV6JuvpHioEa3Mt6e9NMhkzzHYsuBP7An0PgDVCkkUSx3iJLYt1TRVQPNG21GOWLhdnmcmaGFu23Bsduh3pXkYfAp6onlOeih6MnYfcdduNGl2Y/dbmFZxTh5Jdz6mNj4vcyW+HFMT8Qlx/8T0Mem74KvYTc7axKC90bQprL6llaDRmmOVfpMUjoaIh4b7hbOFtoUdheSIPohRi4uQR5Qamjeaq6PkqmywgrkowpDM69S73AnoXPJU/P4DwQ7nFSAhHCqiNaM6ckV3TV9TzlpBYbNkMGsLcNp1NXljeRh6GH3Uelh55XizddVy4nDoa9hnKmLwWdJQFktnQuc73TCRKb8fVhebDpkCk/kX79vkzd5G0SrKCsQxuoKzvakKpEKcA5cAkcuNG4o/iVCGYYaIhFmC5oVfhs2Kpoznj62UH5nkn5CmkK6GswK/VsRfz6DZNuJB7ZX17v0fCH0UzBuGJEMttzjuQFlHkE/jVktf12Tnav1tKHHcdwt593m1erp61Htgek93L3XpcAZtaGh/ZbVdPFWiTnhL6UDVNCwtAyaDGo4Slwi0/8z1f+uO4gnbQdGtxiC+x7TJrhWocJ/knGeUoZBTjRKL4ocMhlKGE4RLh1+GNolDjNCM4pLolyGcz6Lgq/6z7blFwqnJSdOM29Llne2o+6UBaQ5tF4QemyjMMZU6XkU7S0RUfFeEYFFn92x2cc1z+HfWePt8Unsnfeh7vXhleIhxmnDha0VlcF2BW9lUfEtHRWY74zIuKRIiVxiEDjYFzPqJ8Xjlqdwk1pfJs8K7urWz7qtJpdudhpf4kQ6PKIw4iEiGAIVFhUOFHIU8hhSK9Yw4kPuSgJrrn1GnGa0xtry8CccRzwHXVOIw6Y7ylPwfBi8QjhtKI0ot1jQcPc1HElBTVz5etWL8ZsRsFXDVdPJ4KHiVe2h91Xo8enR4endTc1Bv02j1ZN1e4VnNUMFH3UGBN9oubCUtHjwUNgqfAMX2K+4f4oDbSc9iysu/BLgRsCyoxKE6mVaXCpO2jNOK24hphM6F44LWhWSHdoicirqMOZNbmBCckqJiqqCvSbuFwMDKjtIp3Hjj+u8I+JcBLgzuFlwgtCjfMh06hkI7S9FU0luTYLtlcWmWcPdy8XYKeHp5gnp8e4p7FHiRdpFzZm79bjlmdGK8WjdU6EsURmk8KTLHK4EhPBixDTYFafz07+noAN4c12TMhsNDu+i0IqwCpRGfZ5hskxGOQ42Vh9yFWIdNg4GCYoXMhhWJE42mjmiVGpgCn1el9qy8s9G+b8QNzmbWR+Jz6Rby4PtrB6QPeBvUIwAtsTR5PoZFq1AKVf5aHmKVaIlsM3JjdPZ3HHqBe2F5Dn8de5t4rHWbcPlvwmc2ZFVgMldHT7VJpEQGOW8xiyj0HvAT7AlXAJv1h+xa5NjYJ9Hzx67AL7jgr+KpbKDNmcqUWpIDjzyL44ZDhTqFi4T9hAaHtYlwiw6M1JHzlxOdHKInqTiu3bfpvfHIz9Ef25bjKO4K+RkDAgxKE2UfySchMbM5ykDVScVR1VmEXmRjXmkOcBN0THhTehl7SXw3e455b3rRdr53JXJ+bNBn12KGXvRUj0ykRR09TzUwLLQjPBsVD8wIhP0J8zXmjeBT1fnNN8K3vEW0Eq27pECgu5p/lYaPN4uWisWFkoUzhe+BvIWghuGL7o0Ej9mSCpnRn2eldqzMtUC7O8QBzMnV1t7M5VPxLvtZBCYROhnkIoUr5zMmPsZFlUzhVlNf/WGVZUZtAXHRdWp4pXl+ebV6YHpUeX56sHfQctRuxGtVZpJgyFY+U0pKTUNiOeAwRSdBHl0SRw15Av34sO315FPa+NTWybbBGrisrzapKqF4nMyWVJL4jo6J0IavhpOF7YKFhfWDSYfdis+NM5HnlhOafaI/qvWu67emvp3H7M+j2Pbh1+uZ90X+rwjxFKUeByZlLo05sUINSURSClfGXiZkKGscbt1w1Xj5eNt5RnuSeuh5Y3lkd0JyyHGSbjNnamCYXPRU4U8IRyg/BTe5LS0lPRiTEL0Hw/2/9tDq7uFF1nnNxcRru122xa6bpnafa5o1k7SQRYvhieaHN4YLhLiCYYQEh0WJmIpMjzWTOJgjnkqkcq1zsiu4msMgzGXU29tA5zHymflJBf4NOBh+H0IqHDOqPLVDT02QU/RdE2IfZZFrhG6GcyB1nnkSell87HqceUR4z3WxcuZu9WvRYp1hLlkpU7xKvUSGOeEyByptH1IWIgvQAff4NO+C5KDczdMCybXBQruCsAmp96Q4n82X5pNFjdqJfYexh8eE2oLVgj6EZ4e3in+KE5DGlNubCJ5NqAmt07aYvp7GzdAT2T3if+zC9UL/6QjDE0YbBCeVLMk3X0H9R8ZOk1V3XMZjf2hYbuFwxHM/eat5xnqFeqd8HXsVecB193FLcK1q+WRCXMpUaU8eRv4/tzh4LgYmRx3PEJAIi/398ijrB+K42M3Q98axu020Ra70psqeSZkxlQKN2oyeiv6Hk4O1gkmEGISYg16JlIvajpOS9Znjm6OjAKmhr0S6XsIKyhzUoNx15jHvAPmkBJgORhZHILYphDTVPD9DzE1AVJNcTmAoZiFsMnFycsZ1AHpfekd73XkKfBF5hHagcklxA23/Zcxg2lreUQBNn0Q7O2kznCoQH2sXQAx/Bm74gfDg5Y3dhtFwyrDDaLqts3yrRaOFngCXmZG9j9uLPoqThf+DCYUShNaFCIb3iPGKTZBrlr+a959Sp7mt5LWxvlfHIM3c2EXgLuln833/rAaCEp8bFSRcLCQ1TT9vR9VOpleaXbxiomkubAhwbXXgd6B65nsPejZ7bnhDeGV2pnIbbX5nq2RhXX9WN1LASEJA7DdBLGIjVhziEmoJmP9x9g7sQuPw1x7QAcdnvbG1z666qJOhkZzMlSaR3YubiNSGDIR5g/OE04ZmhbqJ6ow9jziTa5crm32ilanor4+5kL+zx/PQZNwU5l3ulfb9Ai8KhRUbH1QnFzEyOgpDHkv8UuRaIGHDZRRscG+HcoN3OXlpefp74Hscet15pXZAdZhyLWzEZ/9gc1sSVQxMskUsO000vC3FIugY1w9UCJb6rO/w5k7eOtQDz7XCy7xLtGyrlqdTn/mYjpKRkGmLJ4dohRSFsoY5g5KGVobMhZ+MsI+7k8CdB6FvpMKubLU8vu/DbMzw0+7g6Oie8o/+9AWxEAYbuCTCK/E19zygRgNRMlYoXAFjk2dKbtZweXWCdrN4BX5Pe/p4HXr3d7Z1pHKfbstoImR5W/5XFVCjScVD6ji7L6AkpxtfFjoKbQAy92HtCOTc2Z7SFsi4vkC2U60op9qhC5pmliuRWYwSiSaIqYQOhkaEQYQ8hiaIRYY/jpiS35gGnZek4al7sXG3W8FfyuPR9tqo5i3sH/VFAOcKyxRHH80lbjDcOIlDz0fQUpFZa1+EZaVqxm1jdON2/3r0eYt8iXrOed94vnftcyZvHG00Z3hkUFwcWJxNN0QtQC42pysRI0gY2Q3VBp/8n/N96ILdfNX8y5/FkLuNtMeuoKMvoW+YAJXrj/yNvYpZhYyDzIOrhCqDroVFilKMcZAplPmYT53ppEis7bMnu1vDIMt510vgIOlb8Dz7AAaOEH0ZqSJALJA1Jzx3R+hM5VQ2WkZiVWjIbZpyjnWsd5J7DntFfPt7oXrgeOF34XNibvtpQmWlYANZtVEzS6pDizcYMZQo+h9hFc0JAQM3+OTtD+Vl2xXRIMlhwPW3MbCupzSfYp4clg6T8o21ioeFy4RbhhqDnINKhdSI/orwjTOTO5bHndahQKhurm634r3kyIjRitmS49bthfbaAZUIuRKIH2Ynli7BN7RAmUiuUMlYNl/yZYhq9W1RdvJ1hHe2eq15nns9el97AXWYde5wx256aVxksFvTVbRM70Z6PjE44C14JOoZnBEiBnT/bvOX6nffu9RczYjFl7txtIOtxaOunuOaQpS3jk2NFoqGiNyEdIQchNSDj4X2iJOM945vk5aZPaAko0ytYLOluhLDmMsv1Mjb9eie8eP9agRuDmAZoSIqK3syOT0UR3FNTFSuXLBic2f8bPdwa3RUd+J3kXliexl6MHkZefd1ZnVKcRptxWV5YLtaAFRsSqlDCDoyMwcofh+MFpIL5QGe9+DtjOXL3IjQesnKwGG5zrCvqzGiLZ+cmHuSA47oh5uH0YMqhXiDTYS5hp2GVIuRjAKQR5b9m/Ogr6jnrny0FcAoyaLON9fx4rjr0PSQ/voItxPYHa4nyi1yOI9B9UjkTjNWPV1nYp5qJm8PdaJ0vnjRetd6xXsbei16z3jIdXdxmG1iac9koVuwVCJOwUf9QHo14C2AJIIbfRDdB8v9X/PW7BbgT9cdzVDGd76ItLyvQ6epnlWZi5SYkOSNTooeiA6E4oR3hgiEXIaLh4CMKI4ElEyVGZ19pBSrYrG2us7BYMlg0rHb2+Uc79f6vwQ0ENgXfSGbLIYyOTvJQ7NMjVHZWX9hCWiNbR1xt3VDd5p7KXnOec560HrZd8x2LnKwb0RrqWhgYi5btFERTPtE6Dheesp5mXsidqJxwmufZxNeGlaiTiRFCzjLLSIjWxb/CZX+9PCm5WbZCc2ewae5xa4ypCGdypfzkKmM54nbhbWELYXohjGHC4zkkrmVAJufomyvK7UXwRbNPdkl4xLxvfn2CPwUcx92K/Y270FqS2pWw1zAZLZqoXC9dLB4AH2Ne0Z6s3ojeBt0am+1aBhf9VdNTmND0Tn3L9QjGBhaCkz/ovP342zZFc/3wyy5wbBipeKcpJiIkMWMLog6hN6DXoKKhh2IVYrKj2GTnZxmpOKq0bR9vsvKa9TR4UjviPk+BVwSayKIKAU25kHHSsNUSF28ZPBqCnKtdEl4yXm0eg96w3nPd99yX256Zztg0lYjT1pFkTsDMh4l2Ri0DI//9fGv5k3bptFyxgO7MrHbp8WfvJlDkk+OV4jQg9KEEIT9gxeF1Yb6jpWT+5vrpAertbJ0vhDIJtQj4DbsRff0AqgPkxuZKJI1LD+OSbRSUVuyYkZs+W/Ydql52HyRftB5LXmAeb90MW+laCRh41saUAxKYzy2MUwnrhtVDQkESvfv6nTfoNKWxZq8TLSiqnOe6Jf6kzCN7YhFh12FQ4XIg5iHDIoPja6TFZePn3WpKLNNvCjIQNLH3HjslfXwAk0PxRmfJVg1iUBzSFhRg1qiYxJq/XBYdKN4L3o5edN6z3fhePR1zm/Ka2BhSVpZUVFKR0AMNHkobx01EiAFCPeR6jLh+NTTyoS8fbYyq66k+ZllkzCNPY1kiBCE0oWhgxWHz4c1jgCTNZpBoSOmf7GgulPHANHn3aToOvan/wINtBdNJwsyajsjSFtOEll2YTZn921wcsx2WXspewd9J3yoeLR1GXHPaNVkJlwfVVNL0EBYNoUrhB3LEucFJ/y66xTht9M8y5m/1LPtrGyjKpyflPCOJIv2hTyFVIS4g0SGT4c8iouRL5ZGnFqpV7IFupLF684W3cfldPSx/vMLvBUMJTUw6DqYQ55OwVgWYD5pg2yPchV2gniEe3J6vnmleCl1QHEma5djTF4DVjFNgkJ/OJosMR+nE/IFo/sX8QDkzNjLzHTALbeVrqmjdZ0ZlwiTw4vHiIOEJocshViG6Imji8qPIpcPnrGnx669tybC+c142OLmK/AP/j0KtxRII5stWDpZQhtOIlbhXWxlI21xca51pHhletp8YXrwekt4q3L6bLZknl21VbFMn0IFN30rnCCpFG0J+P2R8pfkZdnlzMvDr7pXr+KmxZ7xlCiPBYyShmeGNYSwhMCIUYZ+jDOQ25aTnP2kVq5+tojC6sz+1ovjye/S/PEIMRS5HwUsujcgROhKTlSoXspiK2uScRd0Q3iQfB18wnoYeZp2BHIpbNFmKV9dV9ZPq0NGOdcu/SOPFsoK9gAk8xLpQNiyzsPD8bjPsKum0p1Wlq+QBo0TjB2EroP8he6EwoY0iSuOLZcRnQak2KuDtYi/8srW1Grjf+/v+ScHehQYHfwqgTdQQZ1LS1XwW0Nj62n1cGRzUXcmfP1503qudtJ1g3Kta6xnMGP5WKRRJEeNPMwwGCV0GNcOawAe9t7mztwE0jvDsLhdsp6om6DNmXiRzI0YiESGuoJShZqG3IUTiQePlJIsmjGi2arqs7G/Kcn402vgGO559+ME8A+cHbolXjO1Pp5JAFPDWr1izWk6cJB27ndeec57oXtue7V5+3NPcOtowGFFWHhR8ElePBExCidHGp8OGQG/8vDouNx+0R/GlrxKszmobJ//mdSSA4yfiB6Io4MzhMWHFocbinmOUpPdmX2hwqnis7m9Y8jM0ivf9Oug9IoDXhD0GToovDOBPJ9Jrk+8WxNgX2gLbe1w+XaZe3F7vXhMep15LXQEcKpqQ2PSWjRSlUkqPk80YCvLG6YROAP49KXsZuCX1KnIHr5Ns7SoaqHWmc2SVI3Yh8CHhoPhhFeHBIcliKSNEJKxmeWgHKgZsE+88MVSz57cGOrf9OEB3Q3gGPYk2DGPPJZF51DWWbhgt2hsbXhzYXVEeDN8V3z6evh2sHWSb6ZoXGOyXJFRrkr+P2k2vSoUHuYPswWS9nrtMOIt1NDK5L+Ms0mq2aL4m16Vu44KipqFDIOfhWqF+IU7ieWNnpIxlxKeW6Z+sSO34MPLzxLbbedt8V3+gQp0GOIiPjGJO4JGNVCjWGlf/mZPbGNzDnWIevl8DHy1eYR5snaTcS5qqGL7W21TsUmcQPE0hioaHVYSgwap/JbuiOVf1pbMsb83tqOuRqQUna+UI5GrinmJq4S3hEmCRoVyhkKNW5CIltWdGaVerju4ucVvzU3b0+Rf8KT9Rgl5FcQjmS3DOfdCU0sbV0dfb2W7biZzZnUEePN6/HqXfLV4znVwcclrBmb9XUZV5kwjRPI3iSxvIjwVfQmC+sfv5uV1107MgsWStlCsO6X/nTmWtZC7jFSJ4IVSg1qFNYR+iJSKUpA1l0eas6Xkr165oMH0zIHXG+Ty8bL7jwfrEcQfdix6Ng9B6kxKVk5eP2aJayV0jnbld618sHtkfXN5IncAcz5uZmXPX8JWnU34Q8g5pi4hJWMXoAv3/fzwO+Vv2TzLs8ILt2KunqXvniiZyJCEi0mIVYhBg0WENoY2h0WMk5F6lHGaDKRJrMK2QcIJy+vWYeB67UH8cwflEQ4eXSrEM+c/Pkv4U5Neh2SIa0FxDnW0eJ97wXrNe5F4L3hYcjZuyWarXhdakE3XRqY94TEiJEMX5Qk0AOnz7udD2yLQ18Trubyvv6lXnUaY2JFVjSSHU4dXhBOEgIP9h2eLCJGPk6yc0qOXrMyyLr7PymzUIeDA65b4jgT0Dm8bEinrMnA+J0ssUplcQGMua1Rxt3WWeNt68HsQevd53HUgdIVwsmdpYA5ZCFEIReo51DGWJ4YbyA1WBLz1JuoL3X/RnMa9uDax/qkbof+Xc5FXjaOIJoerhI2Ff4OahRaHt4++kRSaV6KYqRWzMb6nx6nUKN5y6pX5YAPQEPEacSb7M5s+Pkq/Uv1a7mLhaeRuCnNOdxd5qHv5fKN6ond3dFZuAWt/YthaglHaRgY+KTEpKTsbWA+1Ben2ruuR3kvUlMmhvAK0HaomouWZ2pLfjZyJsIdQhAWBA4VRiD+IfI14koWZwp86qY2vnLtRxRfUfd0f6ML33APCDS8Y3SWaMgA+lUeQT/1Z1mBFaHdvAnWsdcd5yHsPfD17OnVSdEdv3WneZLtcSVIpSkA/qTWCKuQeYhORAzL5JOzO4WbQl8jyv5W01Kt7oeWaQZbkkF+KI4d+hs2D+IH+hCGK/I6NkDOZFZ+ep1evhbvWxBPQ49ve5Ibzsf84DQwY5iKmMGE63EdET4RZIGOVZn1ttnEgd8Z4rHsUe3570ngidtVwXG3iZTpf8FQBS7pAUjdiK2MeERUtBob6cu1V4ifWE804wta0m6tLpUCbF5awjsyLIIhThueCzYU3hv2J5ovDj+OWDJ5VpSqxJLq7wsvPKdxl5hrzUP5/CTMYRSJ6L3U3MkNlT1BVYF9NZnBsZnPYd+Z52XnPe+Z7zXoseeRxKG0HZW5ds1W/TpdCbTawLXMenhWTCSf8t/Bk4uPXyc0Zwkm4K68gpWadcZbHkXeKy4jxhR6GVoY7hTGJQI1Tj1CWhKC7ogevgbemwjrLVtit5OztQf4TBnYVFSHrLOY3gkHDS+9Wrl5AZdVtcXEedWN5pnrwfA55lXoRdnpxz2x9ZodfOFcdS4NEEzrwLtEhARZQDAb/FPGL5SXaCc7kwcq3Iq+1pXmeA5jqkbOL/ImshjmFRINrhoeJHI2ujiuW1JzgpUyuabWgw1LMjteG48ztRPu+BtARmh56K1Q20kFiTZxTnF1zZGRsD3NQd+F3ZHi+fQ563HuadyN0xm5YaEVj5lXXTzpGczvbMO4jOBhjDSP/mvSd6ZTaxNAMxbG6l7J5paWdBJdDkfONlYeahtyDOYNxhF6H7Yhtj26V8JvVo0qtx7WDvgnKYdbd4E3rtfpLAx8SJR+eKeYzBz56ScRTTF5PY2xps3IadR14CnuHe4Z8UHpOdrxytm6oaNpiDVkYTpJGtzkgMrMl7RejDekB7vSv6bnchtGjxta8hLJoqCKhC5rTkb2NPIkKh0uFLoSdh/mDporgj+iUqZg4oSGp1bN0vYTHLtQ33yPsF/lQBWkPhxwvKMYxEz9rSVBSilm7YeZoenB3dXV4m3tde5p6fnmVeRt1hnCbaXNio1gsUN5IQT4cNVcpiBkjD88F/vRM72Te4tQDyru+OLTJpyiizpvskk6MhYnzgsqGiITphPCGH4oTjsKRjZckoRuq37UtvP7JPtRT3Svqm/ZOAuUMvhnqJK8xWT2xR69TBVdIYrJmd250dK13HXuwem59ZXy0eGp07m85a6hji1whVJdJ5z9nNEUosxyQEbUFb/tL7N7fd9U3yS++SLOurJSj0Js3kxSPtYmehZSF24O3hb+Guof5i8qUYZfDnhOojrDSuXXETtH522vouPQnAKYM2hlFJnMxXDzJRuNQW1feXwhqkW4uc4F1THlBe817E3vfeJN39m/Cap9kqFxVVYJKgkCXN4MqWSAqEpYFzfpY7XbglNX9yPTAubSZrM2kcJzJlKuOkYc0iWKElIVlhHWFhojTizSPBphonj6lXK69uZ/CHM1Z2wrmjvOY/twIbhdbI+0t4jroQ9lOxVf6YUFlOm0icfd38Hhgedd82nvCeZ53/m/uagljSl5qVI9MVEM9OMUrPiDcFDgHMf0m8Fvkqtd0zBLA0bZ4q/ukg58Al8SSK4xBh4mGsYUyhiOHT4dRi6SSUZYcnomnSa1Eua/C9Mwt15fjRPGA/ysHvhYCI7UtITi2QRJOs1Z4YGxluWtpbnR3ZHmzexV7dXkrd8B1N3OgbRBoeV7rVFVP4ELOOh4uGiSqFW4JrfzW8JDlg9m9z0DEjremr7qnGp5WlWCS8YjihtKFQYQahJeEeIqyix2Si5Xjnbeiz6v2tqq/BM9H1nrko+17/aoI7BKyH9wpgDdIQLhL71PMXntlem28cUR2VHrJe/V6yXzJelZ2IXPkbadmD18rWQpQl0INOgUvBiPIF9IMvv0M8+PmmNuYz9nErLf9r/CnlJ4/l0eSNYwliWSFgYMAg0OFmYZBiw2RFJV3mlul0Kx3tY/Ahckn1c/gg+uZ+fcEVBNpHjgqyzWcQZ1JjFOeXOFi8WlpcYhzuXeueqZ9Q3uPeSx3HnQqbfxqgWF1WSVQB0aXOroxbCahGLMMXQKa9Cbn49ve06XFBbyZsgWozZ01mXOUfI2divmIDIYqh/SGLIjZiQKOJpI5mjehy6nEs/u8iccy01rgU+oK+RgDPBFrG7IovjQxPixH7lOCWoBhkWk4cYRzJXlqepZ6VnwdedN3fXPXcP9mb2K6WwtST0juPB80bSbEG+wO5gE69kfrt98T1IHI3r2Jsr2pM6DEmU6TX45aiTWHBIWThk6Ev4ZzhxCPkpPQmVChqqbStPO9EMd70Rvdven/9ToDpw4+GYEl4TFXPbdHA1PBWOph22i1cf1zenaHecl5rXnzect4SHRycJpqXWPtWspR4EuwP780qSgmHpoRlwMK+A7rEOGb1HjK9r7xsiaq6KR4mL+RBpACiW+JnofQhgSHZIl/iiGOr5IhmeKeWae/sP27Ysaez4Pd9eY89Uj/uQqJGM4lJjFROpdF208xWNJghGdQbe5yFnf5ejd8Qn1seiF4rXX8cY9qxGKVXUBTcUr6QXE4mSp3Hz8SXQUx+VjvL+GH1QXK4r6Kte+qbKLPnJGSII2Pi5SIeIXXg4WE34RviGuMlJAPlhOcJKcwrza6HsPs0MDb4+Jr8sb9NAx7FdgiyS4WN9BDBk9yVa9fdWcFcPZzBXcbe1d8xnzlfad4+HYQc6trYmXPXp1Tk0x4QS43PSrZIdUUownM+xHw0eQ/18fMfsLqtsyufaRunVqW8o7piN+G/obBgkyERoXrh0mME5BBlsmbVKQqsKG4a8SqzljYwuWH8SD/wQhBFmkhhy1uOnJEP095Wc5dHGbEbOdyc3ePelV8lnszen58RnUJc21sbWa/YOtVTk5pR0s6AS0UIgkWgQvjAX3yt+ZJ2pzNdsJhuQavuaaWnSuW+ZL1jVCJeYV+hvyBWodJhuqK0JBslkmeG6W5ruu22b+wzOPY0+Ie8BH8fgYnEysfeSp/NsJCH0wNVvBdd2ONbK9ujnOleZB5YHt3fDV70XascxxtRWbjXxtZ4E4pRfA6vS/EI4wWkQzf/UXzOefT2lrOq8PQuCCvI6nrneKVg5K3i8CIq4K/hM2EP4SChUiK7Ix+lNScG6J9rDO1GsAly+fT3eBt7i/6JAYkEjYdqyrDNcA+sUpZVtJcJmP5azZya3SSeBJ8QXtleFl7TXZAdCdw2WZ3YGpZY0/qRBw8pTCTJEAaaAwLAPz0G+qH3DHRJsb6u8mvsqhLoT2YzJExjEqKUYTYgkqFgYL4hvqLwI57lKyadKFSq2azlb32xznVlt1869f2wQS8DsscUymuNGA/e0pNUYZb1WFEabtunHOpdil7Rn0eexV5LnfucnpwyGmCYlBcOlEAR209hDJxKtgcjQ1EAgz3kOq83x3UosdRvFG0Q6vroDSaOpMyjZ+IHIbVhMqFWYWUh1iLrY6hk0Wbn6LHqWKyDL3lxxjPu90/6KD32wHBD18cvibnMX89jEZGUPhaG2XwZkls0HTvdm55Ln3Zep96rXotdXNukGsrZUxdQlM3S2M+rjXgJowchxDdBcr4ZOxb3xTVCcsUvu+z3alNo+CaDpUrjhaJ8IWfhWSDkYWwhhWKu4x4koaY9p+uqPiwebrbxHjQwt3f6ILzuAE+D9EXIycOMCw8QUaKTiBYy2DDafxvj3JMdvt36npqemF5o3jKdI5wKGu/ZPtcWFOTS7xAajUHK0gcnhNlBub4Wu+W39rUb8uLv5C1Eq+ro46cGZZOj3+LZocghu6DMIU4hiWInIxukKaahJ8Bp9WwaLcHxfnR19wd6ZXySv+mC2gZaiNJL4Q6gET1TthVOGFPZ5lrHHRRd8B9NHwAfc56fnd3dkdw3muXZkBcR1RiT1JEOjgbKHcfohI1Bxv91e1B48/W4stjwnG3Ia50pkCeRJOAjoqNe4cuh26ESoVKgySGu4pUkguVUpxQpMytCLkqwSzO4Nve5lvyjP0TCWEW9iM6L4A4PESGS+VWWV3UZhVrbXXddtx5FXwmfD18onn3dxNxsWwCZdJenlZyTTlCYjbILaoiWhU4BzH8OvDe5DLYLM5+xEm4BbD5pL6dFZeOkN+JrYX+hY2D8oSohP6HCo2AkRmUcJ3jpgusIbcowifMhti740DyGfoSCcQVEiHQLQI5N0IlTrxUPF0aZ0htzXEjdxF343hFeo97zHmxdZBxtWs6Zz1gQFUtTahDMTm5L18ilRbpCd3+ffT55o3aONACwu66NK/bqFOgC5fDkZqMCIklhPGFaoSehbWIVYn4jGSVNZ27pA2sNrSxvt/LV9c54fDsEPtmBLoTLB+bLNsynUAcSYhV21yoZeNri3PRdVd49XmPe/l7DXhOdlF0Nm6bZuBjaVYwT3hH8jqfLcgl0hYsC1ICC/Sz6FfeY8/TxFy6G7COp8yfYpbrkO6MYorGiM+FNIWyhJiHJooUjoKVhZyZoj6rmbS+vVzHedaT3uDsmvfbAnwQ9B4rKMM0YUJyR4NSIlseZJ9pEm8bdMB25XhYfWh7l3pXeIZwmW0jacpiY1thTv5HDDw1M4QkqBocEdQAl/Qr64HfmdMNyPi7ebL3qFCjYJv6kk6MQIhlhhSFCIXCg+yELYjYjuyQQJr3oCSofbKUuzPFlNQ33M3rtPauBPgOXh2vJQkzgz7ERR5RPFokYGFpXm23c4B4EnhKetR6/nm5eQd0em4ZZ+Nhq1yKUSJI7T6hM/UohBxyDS8Fh/cg6/7grtOkx+2+M7DuqOqhzZq2k7CNI4lchraE+oajglqG44iFjTCSOZkdoR2rzLMEvNnHX9C329roRPQ+AjQOXBmeJuQx3DzKRd9PnVrkYT9ogW6Wc+91DXoDfGR7SXnvdqB3D3BqbcdkllyEU3dJtz6hNbcp6h5cEskF+PrY623hI9Wcyq+/AbXtrAKh85gnlKKMR4qbiOuEeIJ0hb6HsIr6ix2SCZgAnwmnJ7DTuqnFGs9Y22HnPvSSAdALKhgUJh8uRDnuQ5BOklZIXiponm4tc4N4onx7eQ1+wXyteCF1VW6Kar9lE157VrxLmELnNpUrLCHkE+MGpfhH7lbfztXCypzBP7hVqz6l1544leORBYz5hF6EWISGhW+GxYgRiwuTmZhJoFym0a3LusXC6s491xTmh/HR/IAN2ReZIWIuKjdtQvVNBVYhYQVmFm2/cRN4HnexeiN9VHpOeKV05nBubepkrl9AV+ZLwkChOAcuBSKDFp0KOv048TPjt9kCztfAo7aGqx+kZJ1+llKRMYzpiJmExYO4g+yHUYXribCQRJdkn4yiF66BtLHACM3114jiX+7n+iMJYxW8IcgtnDqMQtxLaFVgXIlmgGvvcWh0/nlTeaN4/3uge712yHKzbG1lVGFpV7ZNt0N8Oogv1yRfFtwK8v2i8f/lLNo1z7DCJ7r1sCml1Z25lZuOj4zWiZqHp4QegnGF54WXi4SMRJVSm4KmeqqXtcPAiMmM1/LhfOz5+vwF3BMqHmotJDhmQspKzFX9WwlihmrAb99193hVfIp6hnwoe/J3E3NBb81nCWKZWVdNM0X+OsEuOCS8Gv4LcgBH9CjmOdo/0gbEZLmprrynJ6KelxqR7IwxisOHn4SrhOGDV4hoiqyNOJVJmo2hvKohtFu+mMlC0zTeiOne9tkEVxI5HtIoHTThQqlKnlMwXCdjlGu9b791LXfIeUJ8SXvVenJ25XPSbj9qLWNfWuFQ6EYiPHowQScHGxMPbgI19Fvp8tyI0ynHD70NsEaocZ/FmDCSBY5qihuFp4MmhSaFXInliEyQoZMtm0ah/KeFsxC8C8gp1ZfdXemx9QcCJQ+AG8kmajOHPKJHMk/2WLdjwGpsb5Ry1nX7fPV7MnwXfQh6Q3UTbgdsKGOjWVNRwEgRPv4xJiewGp4QvAOv+DXsed690qzHhL3stH+qJKM0mnGUeI/2iSWHPoagg4mD3od1hxiO1I+ml0yeHaensSm8ucQl0bHdCemy9cgBaA54GK8jyTGsOzZGLFOqWkNhz2g8cW50S3YpfB56bXxYez15W3S+cSZrN2RvWkNTP0prP4U0pCvjHIcROgeS+Gvsh+Ev1f7IHsBMtPSqF6MXnX6T24/Hi2eH9oU9hEWFF4rph2GNApIvlnGf2abdsbS6C8P8z8vabOng8rD/RQuQGxInxjDCOMlGCk1WWKldTWitbrdyvnhQefR5xXpqefB4N3WccMVn8mVRXThUhkuIQQs3Ei1cHyUUcAk5+iruweI62BrNMcP4t32tiaNdnFKVpY3oi+2Gt4XxgZiCzIRgiJWKF5E9lxCewKUKroS2IsObzVbZZubP8xr/qgpSFcUj+C8mOuFBpE4lVrJfVGZ7bCJwvXU9eM164npQejx5Enl+c0VuWGXIXqRVHEqbQhg6Si3wIdoUXQi0/STx+eR/2Z3MhcPVtQeuE6TunByVFJCKjUKIPIQ1hO6EZ4WYiBOOtZHIlLee6aa4ruS2kMC2zR/WKuWn8Pj9bwnsFQYgYi2hOeVC4UxtVIhckWYybOlwbnSkdxt75n13fcF5PncucoFsZGd9XpRX0ky0RE45jS1hJPMYngw0/ZHwCuTD2YTQIcKbuASws6bcm0eXqZFijG6KuIRohASDMIPihz6IC48nl1ueSKI4rW21X7/qyq7TouJF7fD76QYoE6kf0Sy8OBVAlkxZVIJfA2c4a+BvsnU9ee15Inssewp6+3XhcnRtwGY4YCpZAlGQR8U8ujB+Ii4ZbQ2O/2H17+YC25HQvMVWvBew7aXun1OZLJRdjdSJGIUdgiGFhIYZhzOIGY8xlbKZh6KxrJ+zir2aynfTs+KX7PX4qwT/D90brypZNfU/MklYVDtc9GPoaX5x7XPreJZ7tnx4exx6bneIc7pu5WhAXwNah0/VRyQ9RTEkJ/cYLA+JAjj3F+pP353SM8a2upaxhKi2oK2YzZCLjt6IxoWDg/yEjYUPht6JMI08k5mbhKLIp2WxfLsFy3XTG+C66532mAV5D64bhieoM8M+aEe/UGldsGIdakJwNHTAeTN6hHuqehR7qHbyc59vWGpwYgdaVlIkRzs9+DB1KZcalBFMBAH4sOqQ4BrT/8eQvvyxbaqOorCaiZWOjOyIxIW5hImGn4U5huuJOozBk4uYh6BIp12x3byZxh3T8N4G6fP0JgLcDGMZ9CUIM3w8KkVpUYZZf14aanZwsHVbd5V7h3qNeQJ+OXmSchVvg2kjZIhcy1I9Rg9AbjVlK7gdLxGhBnP4zuu14fHTBsnfvzuyZa2gomOazpMZkRaLGok3hm6Du4EehsOIuI2ukj+Y55++qOOwdLyVxlbRLNsp6ATzYQA+DnQaYiUiMCA5rEbUTvlXi157Z5lvOXM2d515DHv/esF6bXikdV9ybWotZP5cblRUSbU/jTVlKt0eyRIWB+n7RO0d4VjV18vxvXe1kamXoYecFpZYkJSL4ofWhQaFH4THhZKJq4sVkryVmZ5fqGmvcrrbwa7Pt9m45Cvxxf07DA8VFiXkLk07IUMqTotYn2C+ZzhtHXMqd355LXm5fAB7+ni3dkNy52xgZgRff1UXSzVCWzceLcshtBQRCOX8Q+3x583Woc1uwk65kqz1pa2dLpi0jzyM9YbFhDqDEoIMhomH3IyIjeaYnJucpBWt67jEwiHMG9hJ5CLwgvsZCv8UTCE3LkM2TUCDTapU8F5OZCBtoXOGdXV4Znu4enV58XledxF0rGwCZWte3lfiTdpF+Dj+LQEjXRfiCT3+FPIl5r7XnM5dw7m5c7CIpoecs5UbkviMwYkohJeC5YRlg36H14wfkFCTiZtXpHWsh7kEwnjLW9nU4P7ubvoDB3IVfx1aK+g0nEBJSmlW9Fs1Y2BqD3Gtc215GX33e1J6cXrheO9xP27WZt5grFmJTiREsTrZLpIm6RX3DHv7uPMf5vfd2dF/xIy8FLKeqKueqZgvkvSPKog/hneE5YI2heOGo4cxjS+XSZ0NoqerZrXvvYrL7tSD4kvtcftXBqQSlB0TKcA3oz9AS6hUO13yYRJqJHCvc095EXreeZl7rHvfdQVy5W3hZ6FjAltgT7lGujzXMt4jWxiCDkQCmPYS57La09PsxWu9e7T/qEag8Zmwk7KMPIivhpSFoIQZhdGJYouXjOaTLpqxohOtK7OnvS7JK9TE3tHrvveCBDYRhhtYJzYzij/eSp5Qd1lRYtNqc22qdQ11GHpRfOZ683rNdg91hm7wao5hy1luURZIij+SNcslHRvmDC0C1/VT60XfBdQjxo29PLLap5qhvJo/k66NFIl3iD6FEIQHiGyFXopzjGuSNpw/nwSp87GMug7Hw9DV2xTqrfV/ASwONRo+JT0yTjxPR8BR2ld7ZCFpYHLec3B4TXrXezN7nnp2eLp1unEmaqBkQVrVU2BKXz5MNokoTh3rEWUFmPji7e3hatP5yfG8jbTXqiGi8JpnlJGP24jjhviELIQ9hZyGuonIjkqUjZlBoW2oCbL1uvDFE8372t/nQfXTAPgNHBh4JQAvqDoDRrhPvFncYK9pwW9sc9d2dHnte1J8qHwbeCZ3DHQjanJl5lwqVC9L3kBxNrsqqB8mFHIGmPqX7kfi5dZ8yrm+zbNhrb+kcpxZlLqO7Yp1hl2GHYUchWCGzobnjmyRMJgcnmynbawyugfEVMzP2Uvmx/EUACkKrxcXI5ktXDniRBlNNVmbX7NmaG4LcmV37HhEesR6XHwPerJ2QnFRbCFnQV2CV5tN1UI3NqwqaR/vFFUI0PkA8BXi89WrzJHATLcMrpmk5p0RlTKQzIztiPaF8YORhN6DH4puixSQ0ZW6nTCnoq3Rt7zAxcyU2MDjGfN//60KGhXiHuwsFjbOQSdNslW9XYtlU270cYd3ynj/eWh6HHpLeDh1X3OXbbhlrV9/WJBNKUXEONosdyMoF+YJvwCI8nDmsNmfzfvCM7hyrlmifJzEl/2PqIt3hxaGjYP2gcmDmonaiiOOnpd3nPei3awLuK/BkMzT1rniDO7z+mIJsBWfHsUsdDatQmZLLFRWXzNk22qQcJ12pniQeKd7E3zxecJ2cnOUbE1kmV4aVpJR4EUWOq4wOSN/FUgLWP/38YPnZ9ys0IrEq7ZZsFKkvp7ul96S6I27iY2GAoa9gzWD0of/inSPppVmnBiieKrnsVu/osks1dThye5X+SQFRxIwHg0pVDfZP3RKO1QmXfRlcmnwcaBz5nmYech5C3pZe7p0SnSgbbRnIGFFW8JPlUauPcIwGyX7GokOogCC8wfqstplz/rFsbqEsSmooqCXlxeTCY6pimSGaoMRhfKFhofYigWQIJLBmXuhZ6oStQe7XMlH1b3e0+2C9nUFvRD2GvomdjWMPzNIyFLdW1pipGgycN90eXcaeth8TXwpe0V4DHTjbkBoCmUPW9VQPEfAPOMy8ihDGzkQYgOy947pod9g077FGL6psmGpyqCRnH+SGo8PiQSF04Q+gwKGRoQ1ifWMKJN2mniiRaogsRq98cUq0iLf2OgY96YAIw82G5omhDA1PHxI8FG4WS9k4mjZblJygndleId67HyVeEh093O2cKpsw2NwWxFSa0nrPj40MCokHg0SbgfL+cXrEt6Y0wTI0r2YtXSqdaVlm6aUEY2oieyG6IVYhT2EdoQCiV2LPZEZmK+fnKcms7m5xMSBz8bbwua99DUDmwy+GXol9S8pOQZH1lAkWrtfL2hmbix0ZHjlevR6UXtDenl5OXRhbvRqM2XDXTFUsEhWQeQy7yuOHGgTvgfe+czuauFa1KLKl8CVtaGsIaXKm+OXtI5Zi6qF7YXtg56Fb4Y8idaNJpILl76eaqevr8649sVkzfzYv+WV8Y0AEgx7FtwkvzDeOuRF7U0LV1VfimYIbJRysHjjeGp8PHqle6R3vHWnbyRts2Y/XmNXQ0yGQjM4jyz9IPITEwhk+6DuzONl2cPN1L/UtwGtxKSEnbCV2pDXi92GBoUZhOSDnYd+iLOKO5FHmcqdzKY8rqm6ZcIEzN7XkOQb8RX9qQhcFh8iky8LOCdCa02CWHld0mTfbTRxPnYdeWl4qnv6ehR5f3ZYcQVtVGU8YCBU5032QRY5nCs6ItYWngtB/H/ySOQ72oHNf8I5t7CtVqQLnZOXkZAxjOSKaoNzhKuD/YSTiDWMH5DmlVecJab9q6y3Z8CYy9bWxOMg7lr9/AjaE7IeXio1OJlCyUzUUidciWUCbI5wJnXteWx7AXy9e1d4MnZqcqBrvWcnXzFYn03gQ5E6DC9oJCwXYw0X/u7yrub+2kDPiMOduVut7aV7nRiWE5HbiqiJYIgfgqCDRYSAiMOLjY5GlvObwqOwr3K0UsHLyOLVJ+PL7Rr7xQcMEksfyyt3N+I+qUjeVUNdFWUzabZvQnVWdwZ7LXtme5J4v3aZceZsJ2rNYHNaWk83RSQ6qjChJNwZiw9I/zXzl+jG3cPQRcScvJ+y1KYrn1WXxZMWi72KlohfhauBHIYFiEmLJ4+yk3WcnaK6qSC2vr3dyKDVB99e7Hj47gR2DwAc5SdNMwBBqEnDUxZa7mJ8aENvrXV1d4R7MnyUeJh5OXofdPdt3mgTZDNawFAXR0k+MDLdJ4odYg49Aw32QOjq3FrQfMcmuwKxmqqdoQ6btZL3jfaLtoWcg8SEXobUhyCI+Y15k6CXvZ/+qNOzf7sRxznTb90W6l74dAQ0EGYbCSh5MyY9xEVhUvhaYGMiaINtr3TFd/d7dHvjepp4lHfmde1ws2ljYg5cv1IOSBs/9zJFKB8aGhLFBP/5eumh3X/SyciMvqGz06t+oKiZRpS0jYiIc4aYhSOCmoTig8aHD46ckuiY6qCvqkWxGrx0xTzPkt3c5tf2rQGzDWIYPSbOMa46R0eaUbNa52IravRsOXRed+Z5vXi5fbl8QXmRdlhw1WqUZQxeJVRRSbo/lDbvKp8eWRKkBjv5ju1z4Y/VdcoWvyKz/6rioJ2dtZNGj0qLmYa7hLeF2YMEhhCLMYzLkLWWjZxCpjSx3rouxs/PFtsg52Ty2v2PC2UXbyNzLs85IkbdTtBZbV8faodulHH1dvp5XX2fend7+nk8dgRwn2pfY6Bd91R5SqJBCTbAKUgfvxKaB1P6fO5+46DZ/ckuw0C2razWpAKcUZV4j5mKHokbhdOENoN9hZaIqYv0kbqXV5xUpgeuA7XAw4PMKdml5UTwUP9BCnYW1CP8LeA3eURgTcxX0F2zZoBrynGtdn94H3t3ejV66nnOdRFyJWy6ZjdfZFVvSxdDFjqNL5AjJBcfCmj9nfQf5enXOs1CwzC6Z6yepOKeopcpkMaLE4imhIKE6IT9g42HXYl/kI+UWp9EpfasXrapwpLKBdjD5OLw7fwqCB0Ufx82LOQ3bkMLTYpVCmJLZjVs/3L8c5p5LHsDeo95JHkJd8Jy6W13Z1Je/1elTvxEyjqxLAMkfheBCdn+pfI256vbU86qw7q5ia5ep7WeK5UXkuuKHolche6F+YM2hxeHw4lhj1OW4piZo0KtQbW0wEvLUdZX4Vbuj/gqBYoRxB6CKgc1wEFIS7NVSVwqZeBpa3Bfdfh4Cnsee/l7r3pPd3lzsm6kZxJhtVgwUYlIsT1xLycnKRlFC8wAGfQ65z3cL9CbxfG62rIwp0qgoJZjkZmMtIeChB2EzYIug52HI4rVjteTKZvIoJWpSbb2vPDIt8+K4CvtAvhFBFwQhx3GKao1cD0ISlNUJVulZVZpgnGJdpx2fnqgerF66nkdeBR0OW+1acZjZ1mGT1pGbDz5Mv4lvRl3Do0DIvRk7HjfdNN2yHK9yLHdqHKhe5mlk0mNoocIhu2Eq4NNhf+GG4bBjuuSKJrnoW6qMLJJvYvGG9N93uPogvhJBLIOcxzaJwk1MD3ZSGZTYllCYm1q0249c+F2QXxTfA95cnp3d5RzGnCKapdlelyFUihGCD+hMLUpkRy8EAYFWPkt7qPehdP9xoy92rJMqvGiRpsglVqMG4hnh2GDPoUWhVCF0YnUjGeUapnDn4+qpbGuul7ErdD63s7lTvWnAjkPLhk1JtUwhT86Ry1PkVl4YEhohG2uchh5WXe5fEl7kHrReNp003Fra3tkdF19VIRMRkB1NZwqUh5BE0QGOvpd7Jriy9PnyCC+p7ZNq/2h3pw0km6N44mQh/KFdYaShHOGuYpMjgiS/5jBn6Cog66zuU/FAtC+25Tn1vJS/QUM2xl5JHgwtjoaRpZQB1m/XihmpW8bczd2rHnWe7R6Kn33eGB19W9OaUhmBl5gVChKE0B3N50rXyGgFBgITPvf8J/hM9Ywzcy/erghqkij8ptxlqWQVoyqhtyFdINMhgaEnIcsjjyQxZW6nzKmEa/Xtc7CpMyC2SjkHfJw/gQLexYBIuwtNTn1Qh5NDlj2XyRnM23ccOl00Hhyei16J3ySevB1BHKmauxkXF+QVUtMnkJkOaUujyL2FUwJMvxF8YfkQdmAzazCJLiUro+mP50bl0+RNYpliLiDtoSkhUqIZomdi9+Q2JZunEClw6tqtu3EvMwc1+nkde6n/PoIAxUvItUrFDYqQX1MtVZJXl9lWW1Vc+V0qHnMeJt9pnqQeWN2q3K/bWRmhFyWVSdNuEOzPIUv4iJFF+cKaP8L9FLlz9pNztHD7rgor82omZ7HlymP6otvhzmJY4Mqg7WF7IhRiymNeZUJnKukVKpOtqi/IsrI03bicO5b++gFKxKCH34rZDd1QZhMNlMeXJJlwWm4cYZ0LXneefR6Insbe4R17nS/bftoHmINWBBR5kXpOh8wUSO2F6gNzv9R9P3oMtsJz8PD6roFsK2nc6CBmASSlY1tilSGBYRIiDKEEIfdivqN2pSAmnqlxawis7a9yMdR09rhue6S+cAE6BK7HC0oiTNMQCNKZlLxXq5kX2sEb8BzUnf8e1x+rHlXekZ4tnQibyBpHmNcWjxQE0aXPlYyeiXgG/UK2wGq817oXN0a03rIhrtesxKm6J/Dme+St43iiPuEaIVZhN2CQIiGieiOP5PHnH+izqdntLe9x8ZI0qTe1elg90oF2Q/ZGZ8ojTNVPh1JxFFIWdRgN22ObZx3u3cHerF8Vnv+erF1UnW3cRxr2GF7XKRRQEkOPlAzPSXLHTIR8ARX+FLqkdwZ05vHa7/YtCqs06LfmruT1o9LifiEA4Tlg3uCAIeGiGCNJJLvmKqfYKm9s9W7/cWP0j7eLuv19IQB1g/TGeMjbTKwPApHtVO0WAJjrGkQb9F233RXeHJ76XyHe0l3U3VYcSZqt2KUW2VTSEmUPy42dSp6HT8RaQaQ+MrsxeAQ1dXLKL9btams4KP6mj+UwY/ZigaJDYauhrCFPoUSijePk5EVlt2eMKe8sAS6+cSt0KHa1uhn9Lz/aAz4GEMihC5AO5xHW04aWCNhjmhWbmJ0y3TAeoN7QHtRe0B5y3O4ctNqDmUTX4FV80rOQRY1IiotHngSuQfF+LzvG+LW1cfKgsROtimu1aOanJqW+o8Di6eGqoRihEyF0YXKiCiMQY82l9me2aYyr124p8OFzcPYjeUM8db+7AuAGJwlrS3SOI9CmU7SWQlhGWeYbopyD3VAeqB7iX2Ue/p5d3WgcahttWX8XNVVtkpAQls4qy0hIB0WGwyH/FjwluPG2UjNDcOeuOOt9KOtnQ+W+49xioyJiIVVh1uFH4UaiEiLC372lI6eEqWvqxW3bcHGzunW0+N/8Hj+ZQdJGHYj9CwCNttBLktiVhxfdWdebGhwsXYBetV7EnpVfJN4HnZJc6lsu2iTYOtV5EuZQ1k5QS5BIXUXHAm7/gfyHOVi2hvOIcPRt36uLqXWnEOWS5LEjSSKm4iZhH2Eu4TLiDKLo41glT6bUaW/raa1U8CJydHW3+Ee7a76dAbVFA4gOSooOJA/vkqcVQZeFWX6a81wZnemeDl6UXubet16RXc2c5pvJmfgXm9ZHVFCRqk5WjE7JD0W7Avu/8Pz1OXq28HP78MBuiywg6nko/6WRJK/i4CKKokFhVGC0oNsiCiLgZAEltKZVKKYrRCzdb6JyBjVeuFf7Vr6yQbZDyMfQypeMklCGEmYVOJdYmOOaFNuyXWQeeJ7vXs3fat7Q3jrcwduymh5Yw5YTE5jR7k5dzPjJjMaVg6IAAz1qum92+3RhsYtuviwD6g7ni6Y15JtjTWJHIfJhAaFvITihFyJiY8dlWeYfaJ1qgezlrwHyd7UH96q64v0wQRWEFMZPSlmMlVA50hLVGlZWWJdbL1ulnP0d0Z9snqfe3h85Hi5c11vCmm7YntZ2FFsSGc98jPnJnocBQ1QA632zum94DHUoMjQvfSxTazaoVSYbZMqjLeJioZxhimGm4Sphu6Iqo0ilH2YPp7+qoCz6rurxsnQbt146kv0zgGEDqAZnyZ9Mio//0V3UL9Zul+AaMlskHNRd7V7rny0fQp7+3fvc4RtpmiKZR9cD1WbSdI+JDaZKJ4dJBRsBIr4gOnf3s3UQsqEv5iz6awmpP+avZTJjeSI9IZ9hNmCmobthMSHr42fkJOXtJ4+pzmur7vtxpLQxdxI5/b2FgFBDSwaESXiMt46BkhVTpJbbmBuaaBtkXXQde95bnswfLd5MXnddK1xSmuhZGleMFX6SCdB1jZXK7kdlRPJBf/62+5x4tHVGs0TwBa0Y6zHoTibpJVRjYeKX4XjhweFC4SMhGyI8Y1gk8uYg5zQptiwk7l3wtjNPNyf5k/ymP9GCQwYjiHcLZE3ukTDTFNY8l0pZ0Bs63Lpd7Z503qcefd7pXmXdzVxQm4aZulbYVd9S+ZBwTefKdoe8xUKBwr9J+0n44PXA8zWwN61yK7ppAeeAJfMkBiK/4juhuyGUoPig9yJLouCjq+VaZp/pievOrcgw9zO5tkg5tzv/fwlCDcWziFMLWU6TEOZS7NYxV66ZfNtNXJrdY54jXsLfWp6gnnJdIFwsmwyaA9fHFffTbhERTgTLmghSRa7CJL9ZvEe5OzY1c0OxKa4mK3Xp8idb5aNkeCLjIjQhSyEZIQAhY6GkoookByX4Zz5orWtKbi/wAnLwdcH5p/vaP3wB4gT9h8mLkc3UUHJS/RUZWB4ZmpsaXAPdY14EHs2fxB7wHdpdr9yUGsVZ59fxVkRTtNFBzr5L/MjWRaDDDIBOfPQ5cbY0c8Gw+65SLHIpiKeK5crkY2JxYfvhcaE04KTh3uI1olFkASWm5quoq2p6rLbvgHMKtSb4e7tpvkwAoURZh5oKWc0ckCoSJlTElydYQ9qMnF9c/12mXjge4Z7Snqnd8d1VG96Z1tfnFqQU6NHWTtIMqslchvmDRsAsvTN6BjdidBExRe7sLECqXmglJmAkeGLe4lLhyeE3YPRhcSFO4dfjc6T45lloRyojLRJvNrIFtZn4YDpp/ZHBaoQhx0oKTAwxUDwRulTMluOY7hphm0Yc3t4IXlrfJR8cnrYeVh2Am4+apdiW1pJUfdI5D01M5InJRvkD0ECMveS6sjcHtLuyIO9K7QQpsag85lYlK6OIYiAhguGgoRPhZyIKInMjQaTIZgtod6qb7RXv3LHydEa31bp0PRpAzYOgxqQJ44z1jusR15QBVvhYkdpuG2ydDx44X28enl7F3pieP909W8GaYljn1vcU6dIMj+DNMQooR5dEEgEKPb560zew9RVyd++I7Teqjak05vklQCNzomsh4CEGoUNhkuG+IoFjW+V0ZYqoEOpHrJGvMzD3NGy22/nivQQASYNBxj1I2AytjuQRsdPrFbVYJ5nXWyLcuN0PXkveZl8mXvAePNyEW9ka+lkiF7pVK5KE0BjN+krEh2rEUAE3/hc7KnjutP9yPfByrbMq56jNpkElpKMZYpbhRuFSoTvhYSGA4rLi3iR+pX3n/OnA7IUuT/E6dFw2RrlCfQV/3kL/BceIpkuwzkgRTpNaFkMYUlndm4KdBd3LXm+egV7KXyQdwV4NHM+brRjdV4JVNJKEkNkOVItIx2PFTMJtvmL8WjkHdinzfzA8LeKq+KkRZ05lbePw4vxhWeFTIT8hOaFWIn4ihaSV5fCnlul26xJuCXD8c1O2H7nPfJQ/mkJ+hQgIjAv4jgkRAdNOFatXepkwW5ObxZ3UHkBe0d7+3oceDF3AHSubEhmrGD7VbhNqkH3OC4sYh9AFwcI5/9p8hDlNdayz2/APLlArjykiZz2l4GOfolih2qGBYPwg0qG3YerjbuPRpcbnmOlRa3ztqi/d8zt15HiA/AK/esHpBWFIh4sfTbTQLlMRFVQX31lt2zmcB528nk2fHt8gXqkez92rHNha6hprGGRV6dOkEXgOW8vUCJ0Gd0KCf5K9EPnRd2OzqfDCrhzsEGno52AmRCP4Y6FjPSGAoZChIaCr4cBjH2OQZbTmjGm/q2GtZy9GckA1HjjPOyr+pQFmxHkHEYq6jbwQeNLZFR9XJZmXWqvbktyyXjYeTd7mn0zeyp273TbbylpuWCdXC5POUZ6O5QwBCUAGKUP/P/t9MTmkNsrz4rDQrtcsqKnuJ/0mOaTio1oiQWGGIZ8g2iGxYcBjgmPs5Vimgagt6yFtLK/18cl1PvfTO6j9lsEUxDJGmQnrjNjPZdKnlK2Wbhkkmn6bzF0GHhnet16BHz0ehV18nK2b99oh2S+WV9QC0V2PSgyyScTHEgQwQQl97jnQ9zj0tXIPrsztD+p4qCimMWTtI24iYOGAIYOgy+G0If4iYyNUpFrmMidXaoDs2e9PscL0ujcd+r69IYClRD4GuEn2TDQPVhIrFHsVuViJWk4boh14HjceOd6wX4ufO92tHcyb3Npj2QAXeVTs0dOQKEz+ihqHDwPdgMt9yXrD+Ax0zrH1rzjsoCpc6NInCGSYJAdiWyGg4P+hJ6EKIdwiU6NCI9gmHOgIakPsvG6C8hF0nfcbOjP9CoAOQ2pGD0nKjJsPbxFGlBZWaNi2Gcvbnd2Jnlresp7EH4xen12ZnKGcG9q9GK0XVVTJUzkPyc2JimhHXgSRAZE+Ojsut6P1rHLXL99tfGsyaNEm1yVjY+VixmIf4bKhBWDGYVVh+SMJJFBmhCgC6Ydspm6/cSMzsDaP+iX87j+sgsGFoImJDGOOqBFME50Vv1g3WdXbmBxCnVMeWV5IHw2e1x7xHbGcG9rwGUVXKlWhUySQTM1JiyMIDwTcQhg+lHueeO71fbLab6Et4mwlaVgnVWW9JD1ioaIgoU+hMaDnIOAiWWNppCIl0Ce4KUtsJy57MWSz5LXdeNT8In7jQgxFtIiryyyOQZFAE+7V4pfOWWKaohxnHZFeqB6pHtje6t4Q3TjcoVr5GcBXYxWPE3WQ3k3OSviIlMWLgij/Mrv+OQn2frKd8Ihukau2qYHnnCXApG2i9eJoYUthGCFU4QjhsKMPZAYlfWdm6MCrAu2wsIRzfTXg+Oj7Qn7QgYOFEsgiiuhNRVDTk5QVhpe9WTKanFxqXOxeZl5vHtOe8l4SHZwc1dtFGWWXwlZvk/SRjg6/i5qJEgY7wsxAKLzKub92sHQo8OWunyvlaWnn26X6JA0jXOG94QNhcKDGYS3hqKJN49klkqaeaKurYO0HcEmy53WT+RE79/5Fgg4E0sfCiuFNRFC80rtVMtb/mGqbMF0oHRveaF8v3oWe8h3p3eXc/htGmnZYV9aIVIdRlQ85TD2JDkYXQw9/+z0aOjQ3ZLRoMaZu2GviabIoEGYiJDKjOiIkIQGhbKELYOmhq+MhY6Rk2aayaK+qpK0aL7WydDUNeGr6vb5CgWSDwIfTSgONYY/kklSUodZtmR9adRwI3QEd/Z5p3pXelR5a3gccuhwTGuXYSNa1lK3SJ89TTOPJZsb9A7PARf1duex3Y/ROcZKu2qx4Km8oGqYx5LMjRuKLYTYhfKDBYXGhquJhY/JknKZMaLVqHmxHLsUyBDTTN9Z68n4/ABHESobGCcUMcc/zUjZUNRa9WJEamtuGnTyd/17QH3wesl4nHr1doFvPWu5ZVtcO1PHSNc+rzO8Jn4cQBJxBU/4Y+pp4aPVosbLvdeywqvtobKaS5PRjJeKP4Z2hAqEh4SAhI6IHo2TkXiZN6A6qPqwV7wLxcDRhtw16TL3rgEEDAIZnSWeMZ48vkaOUPFZU2GmZy9tFHS4d4d6uX06eQR6ZXjSdM1unGx5YSVcnVMWS+8/sTTvJ1gelBEaByn3/+3U4Z7WjMonwLm1z6lhokecS5QGjnaLiodchWOFYIIchniIFI2EkRyY/p1Wpfmx8bnDxgjP9dtq5trzKwAIDDAY6iRoL/47pERwTxdY82J5aLltZnIedox6VHlIetN553tbdLRwP2umZAJfDlTaSGpEoTYrK3kgSRWBBu/8GO4e4+TWucliwba3SK5XpX6cDZaSkJSLBYk1hdaEfIR7hMOIj4tOkP+YH57tpBavELrQwdfNytfR5drw6PziBykUniSSLc848kLRTYxWB16wZmFsC3HxdY9423qVe3F5pndHdyRxi20CZ5VbRFVGTaFE2TTwKwkkXBS0Cj/+I+/L4xTXGc26wpq3cK0LpzGeW5aSkOCK5ob7hdCCtIR6hDWIAIyOjj+TdJ7QoyWuwLYawfzM4te75GDwVP3LCUMUwCADLN03LURKTJpWkl+tZMhr7m+Ad4l5e3yhetx6t3rNdQ1yb3A/ZZ9jQ1nETotEQDk5LrIjChfODG/+jfMc4yHcts0ZxJm3bK6qpjGhEZgFkEmMbYisg2mIp4KyhtOIY4uhkEmUhZrtpGKqNLXgv37L6da64QbvmvkXBX4TxB9eKjU1gj+ySbZV3133Zn9qpXCTczZ76XnxezB8f3lKdiJzzWv+aFJiLlh8UMFCvTvbMKIh2BbLDM/+YPWn6fnc8synxSm777CIqMWeQJiWkTSMJ4nmiL6EU4TJh9OH/YqYjAiVX5xPpFOs5Lb1v+HJmtMM4fPrJfmMBhwS9B0EKnc0s0CTStdRwFq+YkNqlm9PdZF6nXtUe8p5KXuFdL90hm+CajpiW1meUgRH3TuoMoslUBnrD+wCHPba66XcQdNWx6G8W7JxqTOfO5hzkpSMuImThyOFJIXXg+SHBo2sjJ2ScZfCovepsLF4u3PIr9AV3lrquvWvBSYRxBwEJ8IzND1pSERRU1yxYndpAnBbdXd2VXtifM96FHsSeGBz0W0lZ6Fj91s6UplH6j3tMbEpPh5aEJUDlPfh6+Hfu9LNyCu8R7Xyq2ahVJsuk3iN/ohjhSiF44JYgiaI0YnHjHiSIprAncCorLK9vIXGstAi3jXqi/bXAioPHxkXJWsyP0AzRzdOtFlQYEdmXG1xdDB37HsZeyJ66XkIeP92qm/ZbOVjD1sdUphLJD59NPopqhsDEj4Fr/ma7Ing+dJ9yKHAPbPIqvui7pq9kv+M5Yl0iGGE74I3g4eGcorfjBCTC5ihnjGnnLCBusTEd9Ae3r7nevNfAOUO9xdqI1Mw2jufR5xQ4VbEYBVo+GwmcSh4NnfafAp/7ngWeeV11nGFaUpl81zMVFdLzkF0NX4ppR4RFP0HQfl+78zhyNfnyzy/rbfZqoKkX5knlbeQxopch8+EoIKygzaGXojRjK+RxZXjn1ao4q6ft9PD0M0o2vTmtPEg/TkIBhamJBotVjpPRFhLbVU9XaNlRWzSc952NXl0fY582XxEeSh0n3KAavlmWl+8V0FNekL4Ncct2x9dFasIuP2D7pLirNYpy/LB77nYrgKmep2HlWCQWY0/iIOIpYHGghqFlYfsinaQW5QpnX2j669mtovAp8x92S3iTfAK/agISBVuIdwtDDdhQzhNIFcwXgdklmtWcKp1XXnWfH97t3gMfIh3YXB8bJJnSmBFWHxNhEZhOiIuXCR4FzYLuv2B8r/kZ9igzPXCfbhZsPimyJ08lmSRpowBiNmEv4Q7g+2FuYd6in+OpJLMnC6kpKwwtubBHMlk1YHhc/DN/EUGvhRNH2ws4jUiQcFIA1c1W3RmN2tScFB2VXhpe/x8LXyWeN12RnS6bbZnLGG6WChQgEICO60uHCWKFoQLSQF09PXnY9sl0RDF77hxr3+nHKClmNWR6ou8iQ2FBINehqOEvIdFjAqOBJWxmrqheamatQC/TMtU1Vvh3etf+JAE5BLeG5MoDTXNP6pKXFF7XAFjDWqlcr10Nng8eIB7rnoSehF2XXSJb99oNGLNV/xQ+0eUPQowCyNgGdsNdgPw9FDpfd7M0QLIK7u/su+mtKFil+WRf437iC6ERYbpgQaGPIbhiV6NG5QFmwOhjan6s+S8rMmw0WXeuusr96EEYRAoH9slhDLuO31IMVIsWpBhL2tjbyp1dnjEet56VXwne1J4mnWkbltqFGJDW7xSjkZKPjYz/iZXHlgOugNH98Tqjt8w0nbHfb0YtKGoCaKRmhiSvI2BipSGpYQGg+eD74bHibCL/ZAbmCigAqdtsdW6fsb40jTemukq9qAAJg1ZGZElby/cPJhFElEzWVVhPGnWb2d0IHlqfE19tXwxehZ54XWVc25pCWMaXXxSiEn4Prw0fCtcHxIS4QXs+U7ssOBo1DbJV7y8s96pFaN7mqyUcpD/i5qHLYWdhNKC+4OjiG2PSpAMlh6gOahor1+7qcU6z13dkukx9CUACg1VFwIllzAFPI1G4E2HWQpjb2jCbehwLXaHemF8C3r1eg929XQ6cX5rimRMXHxU5EqSQNg0jScvH1wUlQcH++nt2uKF1o/LxcEvt+KsqKRamjKX1I3SieSGeoWphHSF/4VOikWMbpGCllSckaQQsMK3ccGSzNPayOQ38Ib/0gsHFfshBi+1OHpEk06RVh9d12UkbIxynXYBeWZ6k3tZe8x6dXZFcJ9q+WVgXltV3UsoQfg57irAIE8V6Ae2+yLvE+K21iTOQ8GcuJ+vvKQVnBSYOI94jNOHGIR+gwOGCYWIiXqLMJHmlzaczaRwrG631MEKzKjYJ+Qq8Pf78gZREw8gki7FONVB6k2HVstf42PKbFJzFXbiduh8dnqqe4R40XfdcUNtdGbkXh1Xuk77QFg6My7GIzoXOQqm/X3xxORE15fPjsJBuNau4aaJnseZl5Gbi5uHBYabhMaChIUqhwmLdI9Bl36b7qVlrbe1wL/FyiTVVOEh77b8egcdEk4f1isiNvdBR0vfVYFfU2ULbsxxbHdndxx5Pnzpe2t4+3dzcd9t2mhnYLFX60+lRl08xS9vJRYY5gxM/nzzWufh2FjP+cJzuk2w6qf3n3uW8ZC0jSaJMYd5hKqElYXoiD6J7JC+lAecfKO8qtazF8HfyoDU4eCj7TP4gAJjEcUdPipTNVk+KEnrVGVcQ2RdamBwL3TYdjp9ZXzlfDR6zXd+c5htJGkdYppWO1EHRys9cjLyJBAaXw18Abj0lej/3lbQ7MQnu6Gw9KUPoBeYJJNHjaCKjod4gxKE8oPqhMSI/42OkuGa96GUqSyz9L07ynbU996O6+L4zwGyDvcegilNM+A+iEmCVFdZQ2F0a0Fv6HXadZt8mXx4e9J4NXbAc6dvNmu+YYlaiVJSR9I9kjI9KPIc2xCfBSX3zemv3R/Um8hTu2+ycavgnu6YyJK1juSKDoaWhF2Dz4UhheWK/YzIksWYtKC9qmewDL33xszS4d296dr1fAE8DrMZJycwMjc7RUoOUWhc02L9astu/nGMeZZ5IHy0fP56PXkJdbtwsmviY6BaLlPRR1k/YjN6KHMcPRFhAn/5besS4v7VOsenwRaz9qoaovOai5X1juWJ+4VHheiEaYQbhniLD41ak6GX6J8/poKvc7v7xJ7PXNtr5qn0VQHYChgXRiT+MFA7XEb4T/BXvV+fZTxtWHO+eBR5BX6KekN3qXsSdFtyhWvYZdlc7FKOSiBA2DI+LPEgVRI3Bon7ye+n473VS8vLvkC2Qq7Co2qbFJbPjy6K34cVhsuDZ4SshcyIsIoMkf2Y3p/gpzuwDrt9wrrOYtwy6NnyD//iC6QWUSMrLP87dkWITU9YH19maFJq1nC1dMd76noWfMN4AHhRdRlyI2oIZXNcMFVRTNdCUjdILY4fzhPaByH9/fAu43zZT8vGwLK1Aa41paqcSZTYkD+LfYauhvKDYIWVhu+IA4xUkRaY4Zstp8evxbcowUvPyNgF5Aby8/xHCtoU1yLxK9Q4kULOTWFWv17fZ1pr4XFzdqp4hnmrfbZ8BHnydcxxR25bZUxeble9TNJBRjhQLVkjQxhnCTH+nfDI4/LY1c09w8q3wLFPo7Kd6JSAj0GKd4gbhemFIoKnhKmIK4urkPmWdpuIomGsw7UIwpHJ+NSc4u3sTft3BnoQQiEbLeA4lED5TsJUF13vZIpsTXIZdEJ4LXkmelV9BnmvdUh06mtTZyJhkVgdTW1FfjpbL3ckkBbFDPf/z/Op5brbCdEkxXu5abEWp9GfvJjykpiNA4veg+qC4YO7hCiHyotxjn+UYpzToiqrQLacv7nK+tZp3jru/ftLA+sThh7zKGg0qUHOR81UrFq4ZEZtMnGjdY14AXw5fJx9Anw5eN10xm/qaDxfmlgWUaJGzjmFMWompximDbH/WPNC5ezbitLyxAS6ibIGqAOgEJiTkzWOGIi/hYeFV4WihcWIzIhWjuyTb5rDoaWpGbQKvbLHfdQd3vbst/jWBRMSQR6NKIE1Jz4XSmVSK1q/YghpmnFUdUV5sHmOezJ81HdBdnB0o3D1aRlhclk8UiFHRT1uNJ8nDRxNDjsCp/Ve6SzeRNEDxvO7zbL1qPagUJrak4+Pb4lXhW2C1oE9hNOEpItQj6+VIJq4orKnXrFHvxvHOdQD3q3rD/YoAroOOhkRJXk1Mj3dSKRPRVtwYK1nyW8XdNl3NXoze918wXqAeAx1ZG+NandjIlvdUmtIBT7GN0InlB8TELoDyvda7BzcUtT+yKS+JrbdrAij55nlkkeN74o4inSG6oLxhGWHA4j6jreScpdcnpGnA7Iku7bD+dLn3YPouPOLAnIMfhqcIw0v/ztHR6NPRFg6ZPxnzG45cs52GXkOfJB6enlUeKR1xm+wbKxk7VsFU2pN50DPNfUp+x2XEwsHr/vX65vjQtVUy8++GLcDrH+kXJywlyCP2okZh6WIYIJQhD2H7YiWj4uSmZcznxyn3q0YuoHDB84a3MLmmPPl/34MdBYmJDsu3DuDQztSdVe0XYZoWWqccdx1nHrzevB4QHuOeEl3gXIBbPdjKV9KVVRLjUO9N4Qs/CClFWMIZPtV8HLk4NbSzIDAkbSFrVam4ZuclL2PnYm/hkWFfIbehPiFXIcEisyQoJbSm32kzq+buqzDoM6V2CPmje8D/c0HGRTvIbEuczlkRNdN41NBXdJnsW1ucTh223ilegl8hXlzes13EHRMcPRm5WCMWKVNr0btODEuXh+BFk0Ijf4h8bDlkdoDzkfBa7jAr1mm+pqCloySXIr1hoGHjIRPhI+HF4bfi2+QIJcenRyjz67Pt+rAYcyQ17riIvDU+qUGfRSMIEQt3zcNQ1VKjFQ5X+Flmm3vcbZ16HmBe2Z+RH5nejB25HIkbsZooF/cVhhNL0eEOvQtFyTNFi8LjP568wzlTd25z8bF+bk+sq6nz5/nliCSR43oiLaET4OmhDCDPIk2iu6RcJRgm36kqaw+ttzAWcly1t/iDe8n+sMFKREUHwMpkDaVQapKFlMXXhdl0GhccUFzwnYGe5961nrLeUp3u3KhbbFpVmDfWepOS0fgPF8v+SQ+GjEMZv+29MHq0Nrkz1zF+7scsZuoF6DPmJWS64priQ2D+4QqhqyF0IWUicCPW5WymlmiVKzlti2/Zci801Hf/+sh9+gDRxFCG/ApbTTiPlNJOlMeXJ1jfWpUb5BzN3mnfD98XHkkejd4znKWbr1pRWL0WltQpUfFPkwwvSb2GhoOowK69dnm6dw/02fIT77gsompLqHFmpOTIo72iPeGR4SigtmDPYZwh4ON6ZE+m7+fXapBs8q+ZMjh1NffkulY9pgDKQ7kGmwnCDPYPgBHe1HbWfZgEmhDcoVxyXd6edx8r3uSe3F3BnLCby9qo2QYWQFUlEnLPtUyQyomH+wQ1APn+LbtdN4y1AXKbbxFsnirMaJBnK6S/Y6wimiG1YZFgw2DDoTaie2Md5DhmXahHqg3sO66LMUg0cbaPOpY9mQAeQ+WGSklCDFXOz9HQVBDWr9ho2e+bBJz4XgMfDt7b3w/e6143nM/b7BqVGQ8XWpSiUn1PjUzfitgHL8QhAWL+MDs8d9x07vJ9r2qtP2tt6NlnLiV6Y0fjMiHroXthFiEmoXbil2NSZImmMud0aV3sKG4hsVTzyjcn+ch9CcAYguIF6UheDEAOddFl01lWRtgXmXmbot0EXbGe7J8BnnUeVx3PXWxcOFrvmUnYCJWvkuYQJk2SSq5HwkRfQfr/HzvHuTo10rLuMDRtHGtf6Pcm12V9I9tjD6JR4Xzgf2CQ4dBiVWL1I88l8idfaYxr9i118QY0OnZP+YH707+DgrcFAwiTS0ZOMVEk086V9VfKGZLb4tx+nSMeZV7BnuFe5l2EXW+b6htMmfPX+ZTfUsuQ4I4wi0cIq4VBQlX/QHvTePj2XPMLMIZt8ewJqRbmsKVtZEHi42IHIeAheeDzYYlhzWLQ5CVlMmaEKTtrbO3VsC0ywvZIeVn7777/gj/FGsfNC+5N7ZBWUw/VzldI2X9a2txtHXSeXd9Q3yYeT55OHUzc3FtPmaMYD9Y2U/QQq45fC8zJOMWKQo/AGTzWOat22zO/MJXuEGvQKcznmCTNZJDiieKGobThdGEl4XMiCuLJZARlu+ZgqQDrCa1Wr+/zK/WGuHw6xT5iQa4EtIemCl6NVJAbkk3Usdc7mIjaS5zv3SCePR6g3oifY94uHYic7VsxWdxYvpYRU57Rxw7UzBvJaMYcQ/A/uDz9eh425jPfMbbupSwGai6oDKcM5Fqir2Jo4V1hNuDPIaNh0+KYo/KlWWbIqT5qj60Qb2CyTPTcN8X7FP7DgVAEKseMCsXM6A/DEqpVLNcLGTBa+twl3WJd0l6BnrYeyZ5lXccdt9vFGlZYeVaUFFBRlQ8OTLHJgkb4A8/Aqb1RejU3h/TN8civI6w/akpobOXVpTTjbqIqIVLhbKDooQwh5+KZYz3kaCaq6OqpyK2kL0YyBfRDt0X6q/3LwMyEakaRCbdMoU+1UbWUYpbAmHyasVt13F8eFx7onwYfUV7SHe8dehub2kFYutZe1JeSZY+PDXkJ+wbmQ8XBFL2Ie2r3xvVLcoTvkm0HKrUomWaP5OAjKaKyYdEg++FHYWEhnOK4YsJlLmWAKBXqguz87tfxkbPh95d6i32ywByEBAaUycoMQA9nkWsToJXmWAOah1tx3WadMV5yX2dfGZ6HHradghx5GrbY1BadVLVSek/uzOYJ18dfREPBrT4b+yR4ffVYszQvsa1GqwfpL6axpUBj+KJhIa1hFGFEoXIhZOHJIyikeWXJ56Qqfmu07osxYLQFNzj5wv0pf8bDesW5iNqLwY8fkWwTY9WGmDUZ1FtCHT7du56BH2Beh5733iOdihy32y3ZuxeMVTZSTZCVjZkKigfYxSlB0L3dO184mjVn8tUv1y2v6xMpe+d3pTmkF2J0IaUh7qEhYPzh2+INIpjkaGW5ZsApxGxirh/xADOJNnV5Cbzyf0mC10W2iK+LsY4qUQlT4pXxF/uZYNtxXEldvt4IXy3enB9xngJd7JyKW3zZR9fslVcSv1FpTcNLicg1xMAChH76u3S4eTXSs1Fv/e3+66bpFudapbZkAiNDoeWhmqG8IODg4GGzYsakz6XLZ0sp3CvsrRxwBDOjddk5Gvwk/vQCIMVwh3pLNI4pULcSSRW6V6PZaRsknAedB54E3u4ezJ73nkJdg1zWm0YZqZeyFheTaFEOTp1LoQjZRjoCgH95O8L5TzYE87nw0K6o68opiyfFZg6kzeNqYh/hoWD34OlhFKITon3j6uUjJs+ooqsNbVZwJnJPdWW4FvuDvzABlASrB/bLLg2hD+8Sq1UMF62ZBVrMnK+dqN5gHyNe0x92Xnndzp05m7wZbBeX1ehUVFG6TisMEYk0hdfDVsAU/UL6CPZ6tEGxZe4rrCap1ufhZS9kbSOkYnIhqaFGIOuhhSIHImhjdKT/JlCpKKrdbd5vwjM4NUr4qfsQPl8A4YSqRrSKA81rTwSSUlSoVtTZvlpF3D/czt2Gnn5e0l9gnrbeWxznG1saLtif1kgUn5JszztL1ElRxtBDq0BXvVU6+/bndIwxnG/qrRjp2Oe2pg6k++N2Ig8ifuFJoWJhMaHGIpEjiGUNZi/oouqDrXYvgvKCNV93yjrDPjuBBoP1R19KFoy/T3/SSRUzFuwYlNpGm+Yc9N1lXiPe057Jnkrdop05G5iaGdiGFvHU4xIazvEM/woPxqUDysDWfkz7LXdCtNkyG2/QrKHrE+hg5salGqNmop5hzGEI4U1hVKGIImbjtmRYZxfogSnCLD9ukrHn9Kn3PfoJfdNARkNUxtnJ9cwZD0JR81PG1rpXyVo323pcpx1bHuOe2R8HXrvdzZ2HnA+baNj9Vs8VWBJ6EBgNC0p1x3qD2IFfvnI7NDgONYayFK/SrgerDmjh5uQlaWPrIgAhiuFIYP9hO+EsIhAjLePXZZjoEKopq/OuDXGA85G3IropvN4AIIJohn3JVswLzwURItPGlkTYEFnd215dPx1YXm5ejR8F3r3emd143EJa4RlHV4NVchJ/EB9NsAqbyChExMIdvs572zhZdfyzAW/vLV8rDOk7ptolJOO74i3h5mEoIL3gjCHN4gNjTyTIZidm/ukuK+8ud3Enc0i2prkMPOy/PQKyhRbJNAvoDnFQ+xNuVZ+YGBnrWu6cCN5uHqRfHl7WXw9eA90gHHobM1lgF7nVBpKiUI2OQYtiyNtFKcJTf4I8MnjC9jHzLHBNLaorfWkzpxYlT6PsY0NiQqHZoVjha+EX4jjiqyQdZjumtCltK0dtwfCCs5e2LDiOfEP/r0HIRWBI1cqgzj2Q85MA1UTXR1kzG2rdDV4m3gRe3x7p3lSeZd0EXNUbUZnJV/fVwVO0kI1OtMuliO0FigIKv3v8YnoQ9jTztHEFLphrlCmG5/olZWSJYtIiCqHr4DAgzGGIoaBiwWQDZNFnv+jhKz4tp6/FMv41vTi6u4R+m8JThL9HZkrszcRQJxIs1UHYPVjGmoWc8V0mncCe/p7snzxeO52y3Gzbc1mxl/wV91Qj0XHOKsuFCYyF9UKuf5r9YjnB9wr0AzDGLtEsWSovZ9DmZiRH4xFiJ6FFYYJh5CG5ITpiCSPBJUGm/2iQasqtVfCAskN1rrfjO2n+mwKMhKPHTkn8DWXQCdKpFJ/XupksWkrcrBzQHjKeop8VHtwfEx2XXIlbxhoJGLyV1ZROEcEPZcwUyWOGPEM3QAe9Wrpf9vU0JHFxbs8syKq5aBkl9qSqo6AiY2Hl4SMg+GEzYVDjdCOPpRzmQmiaaiYs8e9TsdM05ffd+zi9mUE1Q/cHMcm3zELP+RHflNmWVFkiWx0bxVzx3XNebJ8e3uSeml42XWScO9p02O0WqFPiEnQPRw0uyfrGsQRCgJD98Tp0+D70bjFuLo8s2SoEKNcm7mU9o6HiUaFrocug0GDcYf8hsaNlJJ0mP6gMam/sSq96cas0YrcNupQ9JsCIQ04GnsnkTPhO3VIg1HIV09ipWf0brVze3WFejR76HwXezJ4OHRYcYlsFmWlXFtSUEnaQHY2/iexHkgSgAWT+ZnshuGC1JbKOL64s+aqV6SRm6KUB4/3igqKJIc0gxqDGIeGicGNBJGXmPSfEafLsly6YsWezTPbd+fO9BX//wscGfQkFi6tPBtH/lCyWBlhu2pvb9VzRHRHe054+Hstej15TXUxck1r2mS+Xk9W2UkJQeY1ASyDHRsUjAac+gHsb+Ce1I/KoMB8tner6qRfnN6U7o3Oi3OFYYOOg2OD44b8hhSNtJGllJueYKcMsWu4ZMRUzRDcqOfk8iD+KQy/GQgg2C+7ORBFh02mVAxe42WgaV5z3Hf+d+x6A3s9ecp52nTicSFs4WPtWwtVX0tDQ7g4FyxqIDQWQQiA/B/ureU02EfNqcBGuQmtCqa2m0qXcpHejLOGZ4NchIWEIIZLh4SMaZKylUGdk6KXrca3WcEiz1fa/uO67x/9JQshGG0fwSy5ONxDSUzxVzReA2VpbLNxwHSJeT97HHsXfVB7T3cGcUlt1mQQXhBY0U54QzI4+i54IdUVagnP/73xjeQN2nXOFsKNujiuoqbMnV2VNpGmiyuIx4S3hHqERYOtiCWKL5AclYCb4aMXqxm37MGbzEzWm+SV7AX5twcQFvofSypNNTJC0kvgVQhetWSQajBy/3X+eJF6uHl7e6d3UXiucapur2j5YHlYQE6RRFk8NDFUJJkXzAk9AZfxv+hC3JrQm8MjuouypKYtn1eYfJJ7jmCL3oXbhJODb4XUhoCMFY2alfea1qGqra6zHb57y1fWDuIo7eP5KwY6E9gdPSc0Nd1ASksiU8JdKGQQauhvi3VeeGB7j3leeNd6K3m0c2BvnmenYPNbKVCMR788jDKqJWkbmQ2tAZf1vOg63MnQvcbgupiwBKcnoe2ZEZQfjg6HgYZUhL6B1IKhh8yNp470k4OZCqCzquWyT76FyQfVL+GU7P/5MQR0EhoeXCiiM/Q7SEgmUwVaKmO2aLFv0nIBeEh6EXx6eWV5yXgMdZtus2gHYVZZRFLESio/czLXKcUa/w67Azn3g+sS3nTRb8iwvCqzTqe6oNqXFpRAj7CJjIXbg3qFqoPFhuqI4o1skjCZPJ8uqI+zUr1ZxjfUcd4c6sn1WgDUDcYbvSeuMhk9LUduU7hYYmFHaD9umnLTeON7cXzHeh95dnimdKxwFmtPZAFa7lRpSmU+qTRCKDEeCBJSBgT5cuxZ4PTUiMrEvjm0/qyDoQuaYpJUkPCHJIalg3eDK4ZGh1uJaIvVkoWZ+J5qqKmwW7snxizRwtsD5j306wDxDG0ZlSUBMRs8+kdqUORYE2LhZ7Fu9HPJc414rnvQe1p8YnaCc3Rxd2v/Y/BYzVPOSX9AkzS7KKIfbxOuB4T52e004YDW+srPvV22B6wro72ccpQskGuL1YXqhc6EWIeZhhaLFI4pkeSYOaAwp2awNLwNxN3PyNow5mvyUwDQCecWByTWLB47eEXCTT1ZwV/HZ0dt+nLQdeN7eXtkfOJ6eXlFdEFyL24UZfJdo1Q2S0hDfDZLLeoeWhWnBaD+Du+y5PnXHc2Cv1S4FqwbpcObaJUPkGiNwYdqhHKDUoPFg2OGeYz3kG+ZsJ1PppGup7oww9HLJ9mD5YDxJ/0DCewVCSRyLV46ukObStFVAV55ZZRtGnAFdlZ4V3t+esV5onjFdABzE20xZipfsVdzTOhCkTitLGghvBV7CjsAA/Sf4knYGs68v4K60q5GpZSceJblj6OKcojNhIqDIIP9g+qG34znkDmWH55moh2trLWLwM3KntZY4rbuEvv7CTYToyCYLVE2yUCeTclVp1xYZdFrYXHhdBp6mnpLe2N5U3qSczd0Km5YZshgE1ifT+dGlztlMO4gpxjoDoD/ivHO5IDc0c5Axj24/bB+qGugtZoykRCMc4YfhTKDEINvhACJ/or+jU2UbZu0ovWpzbS0wG3KU9XH4f7tyvpSBq0RKh1VKiE2xz1FSRFWQ1y/YjRtuXHDc5V5iXkrfGZ95nmAdwN1LW/MaKliz1cwTzFGhDx0MOgjehaDDDcAMPPg5kLb3dG1xAC5drNiqRqhgJl8lOSJBogWiLaBAobWhOCH9Ii6jguVYpp/ohWrH7PtvlPIuNSb34/r1/YZBgkSgBuBKQM0Sz8fSkVTcVviY5Fr4nCmdUl4I3rhfSl6DnvidcZyomwhadJjM1jdUsJHEDzJMTAmvRsFEVcDGvb/6SvdJNKBxsm8hLKzp6egv5mDkvCNQ4mNhdSDoYSxhCCFjonGjCuTi5hPoXmpe7OhuhnIltSX31TsMfgYA5oMGBvhKSgw3D2FR1hSLFrCYm9pnG4YdOh1sXgHeQd7oHpEeE51x201bXliXFvWUeJJF0CVMggsvBuWEPQDYfch7E7hWNZey/i9/rXrqhuifphLlMKOBIoDhbOEOoJAhUqHH4ivjECTyJiCoPaoFbKmuq7I0c9R29PocfVCAOANlBkyJLAxDDx+SC5R2lp7YD9p/W3YdJh3HngZeyJ7aHvieHt1w26raEZjLVsgVWBJk0LzNAIrLh9yFJIHh/cC7y3izNLWxiLAq7QpqYyjj5yyk72QlImIiGqDl4NThZOGZIidjAiTsJY3n8KoRbKzuZ3F2tD52ILorvE+/bUJ+BXhJaUxRTpLREtMgFlNYNNl0W7Tdeh3oHlleid5qnnveQl2SW8EbnhlPF21VDRNdUEhNpIs4CHuEjEJIfz97R7jCdmvzfzBP7horZKkJ54RlHOPj4ooh0WExoL3gm+FRolmjHyRT5aqnlOjVa4ouRLBYsx+2CHlI/Gx/qgIWheMIxEuWTdbQv9MJFbQX6lm72yjcBN1iXkcfU962HnUeOB1zXEea6Zn516gVgpL4kBWOdMtViJCFMsLd/wS8I/kcNhgzMTAUraursal65oNlxCSy40Bhq6G4YO1hd+BTIWEi+GQpZXgmvOnEKyGt2e/nctZ1+bkcfD0+gQIgxRxITwsDjYJQ9pNVFWmXSFnKmxFcbd1anmkfIN8AnrbeDR363GebNJlNGCtVp5QGEM4OsgvxiOKFyAJov0e9LPlmNtA0LbETbnlr5CnopsUmUeQ4I4IiMyGBoXwhMWEEoluimyPdJQxmVijK627t66/mMk/1jfgTO/v+IUDtRJjIFIr3DbVQbBLj1M7XU5lV2u3bkpzg3lCep96n3uZeFx3eXOQbRxoeV+HWPZQj0d+OrMxYyRyGdwPSQBu9JPoz9tTz1bFeLvNsM+rBZ1cmSmTYIy1h36FzYbGhU2HfYbLiRSPZ5O+mTqkCqkrswy9w8lO0yHeyOok990DZRBLHuMnXTTsP+FKiFQ5W31lamkPcAl0r3ecfRF7v3yieoV2pXJtbl1rTmDcWtRPokaiPT8yWybAG0MQxAJw9Xfo39300mbGvLuFsQ+niKBPmdeVRY3ziR+GFYQOhZKEwIcpigaNVJRpmbCgH6lLsqG8ccb702rer+rl9SIEyRHrGdAmoTHiPaxIw1KmWt5hgGo5cIR1A3hwe6V8WHvBeud2pHOzb51pS2FfWwNS6UhBPgQzdyYmHEcPcgLR+EDrN95C04zJt762tSKpCaLtmDmS1Y0gi9+GL4Zdg2CENYfUif2OTpHPmBqg7KcesPW92seEz+LeBemF9SEC6AwXG7AniDH+OwVFelHDWUVhVWiTbpt1gHfueFl6RXsafF554XTKb5NqM2IKW+hShErnPrY0EynmHmEP4QUD+nHtb+Cd1r/K778Gt+SqNaLqmXCS8JBLiqqIjYXthDqG4oaeiOCMD5PdmAyfDKcJsMO3GcXRznHbmedx8wn/mgkxGBYh2i82O/RHrlB+WLNgjmjAbb1yLHZieT17EXy1eiN4+HO3cWNrYGS/YLhUuEocQe01pSy7HqQUTwcr/HHuOuRU12nKe8BDuHqsNabNnpeUU5FUiqGI4YQzhZ6ExoU4iGyLSJD/lUifWqZor8S38sKYzh/ZLeZP853/qgvJFvAhfi7ZNuVDmUueVetg8mRDbnNxbXa8eZJ8QXmjefZ6lnT7cJJqhmWqXXtW5k0rQeg4oixPIcAVJgjO+/jxDuXq1/jMw8NUtwauvqZpnbGWmJGHiqeID4UDhGmF2YVciICKfZH8kxGd8qU3rdm4W8CizPLW4+Vq7tf6kggQFFMfay3POOxAzUukVORcbmX0bGZxDXazd2x80XvHeip6v3ZmciZvfWcCYJ9Xhk3IRe85OC6LIjwXDAoR/UXzXObG2AHPj8OBuSGvTacsn9mX748ji8+IFIZRhceDpYYziIaLNY+glrmYxKQ1ru20XsDqyfHUVeNb7fH47QWXE0UfnyxFNhJCUklqVd1aoWInamJxQHhyd5p5eH1weYt58HcRczZvg2ljYTlZGk5JQS06+i+oI9AZ5wtM/x70p+h72mTPRsKyvIKxZqVNnl+W5JJmjp+J4oUdhHeG7YONh5KJp454lX2aF6P0piiyEL/Jx1jTiuAH7iX5tAMOEfscPiezNfw/NEn9U0NcZ2G9aDhv6nM7eQh6tHtvegZ5wngwc1VtRmhDYHFZDlItRu48bTGIKJMZJw4hBPjzguqf3cXT4ca/u9CxpKlSn02ZbpPVj8GH5oawhPCD0YSfiNyJHY5ak9KYFqNrqEC0WrsjyHDVZN6d6772RgOrEKIbIinnMQc9vEm+U49a7GIsa8ttfHWDeCB6yntifGZ6OXcUd+JuWGksYm9aLFRNSdg+UjDmJ8oZtBGNBEf1ROou3wDTLsfzuB+yv6kYoRGZ8JNBjuqH64hhhDCHS4RhiOKJoo2kkyuWbZ5nqAWwrrphxeTRTtvY6Yv2rwE1DjYb5CV6MJA+Ckg9UJpa9l8sZ5BsvXOBd9J6s3tse6V5t3hQdNdvwGvZY+tbJ1GUSlhAzDSeKukdExK7Bub3UevL4t3Uz8gWvs+x6qu/pRibspQEj9CJCoclhTaDb4V1hqOILYsUkrqYfKDRp2uwIrrnw7PNUtu45nrxtwC5CyAZYCXwMBA6NkRPTyxXx1+vaadu8HMWd4F5mH3Ze1V6THkCdQhxcGlUZQ5dFlQHTKJCCDW7Kv4d3xRTBq364u9t4n7YLMrev0+31qrzpPSaN5ehjU2LnYgXiKyFVIPXh6CIp4s6ktKWhZ5UpcitXLggw8rPfNk55STz+P5wCDwV7yB3LFs6Z0VLTq5XdGHTZjRtRXIyda94QXsmfd57V3j8dQ9yVmugZVpdSFXKTF9C6jubKxIgQxbDCB79TfBM47DXPsvjwVa2Va6zpXmc65ZHkZCKDoeKhRaAYYcZhF+FHYvMke2Y/JofpSStlbUxwo7MbNh948LwTP3tCFQTxCHuLXM2NUOmS6pXDmBzZsNqznIcdnt5mnqve+N6WHfEddhxI2o1Zblh+FeuTVtEKDovLtAhRRepC03/JvFN5jXasszDwsO5va+1pxaeZ5aUkW+LuIlXhaeE0IULhlyHpIoWkDOWh5u5pHKrY7ZDwW3KbtZy4sDtAvphBlgUkiDwK0g0DUC4S6JURFtKZTpseW+Sdcp4a3wJezh6PHtId9Byv27NZ/9gh1oOTylEoD39MNYh7xcFDHn/pfLk58bbUdBCxN+6XbB2qR2dzpZ5jt6MiYhIhXmFQoJJhh6HeIvQjyKUB5w5ojKrr7P/vT/JANLA3zHtbvk7BQUSCxzlKkIzoUAKS1pVl1yUZHFpOnFMdW14H3zSe+p7fXpSd0RywW4Ea3xiclkKT29IZzxnMVMmHRvPC7P/XvdW6oLbvNLtx8O9bLE6qDSgSJUGkzePy4jbhR2FIoO1heCEPIqzjeeUiZkrn52o8rMQvljHXtYh3/7q4PVDBmsQrRtQKQ0yXT6sSWxT8VnkZGVqFm+IdKl2s3o0fT184HmSeJByPW8Ha09jB1rwUrdG0Dy8MQQofRthDVsE0fkP7LvfdNMNyHy+G7LlqT+h9phnk/qO54k+hvOELYUuhIKHrYhJj+mT0pndn3KomrAXvG7F1tGc2+3oWfdaA5EMxByrJacwEz3BRlhSbVqfYcdq5XEidB54hHrre1N8L3qZeKN1z28VbZBhFFsnVBlLNT8WM8EpNBx9EYwF4/aX6eLg+dPky6e9w7Sgq4OhDpn0kYaOBooAhlmFWIV2hImF+4mtjS+Scpj8nsSm6bNDvPPFKdF03C7mpvSdACwK2BiAJUAyhTlXRB1PnFmxYmBo2m1Scy12e3rpfPV8bHk/d/Z0DG/garhk0l8jVa9KKEAaNvcoSh7dE+kHbvpe7t7hJNkzzKXAIrUzrVSjmJx6lnSOIIrriHeDSoSMg6iGSoZ0jGSSNpc+olGmWrCyt8XDFc9z15vnPPMx/8cJWhX/IIAwfjkbRJlOsld+XZpmuWwfcnN5U3lte3l6X3p8d3t1pHGwbB5lv1/0VQ5Mc0SXNSIrwCAlFXoH4P1o8e/ls9dAzDLBCLdlrT+kUJoTl4eQvoyRh46HVIX7g++FuYrRivCP4pQZnnemXq7gtuTB0sxn2L3kMfDO/J4IvhMYIrgtCzc9QqZL0lRpXQZmjGo7cVJyNnpEei18pXveeAN3HHN4bexk618RVYVOE0WQOh8uNSJvFfwKuP6f8CvlMNlXzZ7DzLinrqymLZ0/l0qQkIupiGyGTYWOhDiFBokPilGO7ZXAmpCkaaw3trfBi81H19Hh9u2B+zoIgBR7H08rVTXzQWxJyFX3XMhk32xcckV2X3caest8fnoUeAZ2YnMybslkqWCvV3VR8ERaOnswsyQsF6wJ5v4P9Q3mUdsd0UvGGLqRrTKnoKGwlqORiI1AiB+Ih4TPgmOFWYbxigePIJZSm+ahDaymtGi/U8ph1ArgLu4q+kAGpRI7H6UqgzRyPndI0lQEXPxj/WlJb/lyknioebx6zXkbemV4MHMBb/5o9GHTWbpRCUeqO7kwuyRZGoANJP8+9fLp/9z00KfGl7yGs/KnZJ7/mB2TM40EiuiFP4SagtWIz4ZFikiOFJUzmpOh9Kobs8i8Icnl0lvf8Ouo9/cC6hApG8Up0TVJP9VKwVIiWZBiVGnnbwB1wHUceAV8QXyGegh6W3XXbxpoN2HnV+xRkEYOPh4zkye9GeURIgP79h/sY99x1NbHjbtAtEyo2p9Rm3KT6o6Ti5SE0IO+hLKE6YboiumOQ5Ohmvqgs6kssnS6qcjM0CLeT+dW+TICexHuGlEllTHmOzNGRFAvWldjUGgIb9t0HnYheH98wn3dfNB0gnTHcR1pL2JMXS1VIEoOQcc1BSlvHCUQ5wQT+P7rAd+f1EjIsrzysymrvKIVnGKVSJCSiX2HRoQ0hHyDaIcyiWONMZGYltWgS6nar525j8OR0fTb/+iX8YoC1gxDGWkkOjGdPF9F6k7ZV1Bjc2k0bgZy/3eMepp6KXtJfId6S3WccmJroGVrXKFU3UsOQIc1OSo+IAsS+Ab8+drsP+Fk1RjMTb87tUesV6EqnFWU1o/9jFWJYYTxhEOE/YYsiOSLNJGnltGdcqeqsIC4/sPCzg7Z9+eu8WgBfApmFuMg4i/yOXtCBlBuWNBeumjTbyZxOHboeo95Dnsce7h6anVRcTJseGT7X+dVSEt/QrQ2LC1vILITegVL+y3x8uPp1mjNlcA7tg+uZ6Wqmw6WJ48bi86IdYf/gueCjodphrqIyZArly2dnaUzroe4vcHazPTYluOb8kv8egnOFowikCyxN3tBj0xDVRRa5mWqbcxy3nUCeBZ73nwKfCN7y3SwcT5tj2Z2XJdXLk0QRMU4ZS3MHwEWewoP/fXvieOa20/NBcMpuMmvTqWTnQCWKZBzilqJJ4gMg06GPIVuiVaLd5IXlgWfmabKrpW3nMBUy7vXseJX7Rv8AAj3ErMfpioVNdRC3kxVU7hbRGTja4VwL3XDeCx8MXm7ecF6MHfbcDNvpWe6YNVWhk+dRaA56S6HIUgVGgkY/jPzIuWf22vPN8N4uXet1KY8nJGYjpDejZyI4oVYh+CFTIZfh8GLQo/olDub7qLCrV2z+b1TyTnWqODD6w/6EQaeEjUeECoONC1AfUksU6VbJGSGaCdxRHR3d/t7XHy/eqZ6E3jqdI5w32eUYQRXL1HnRcQ6gzPAJIIZow2KAWX0rOjJ3E7Sq8bRvOKuxKfsn8uYnZJgjjKK74YGg4SDD4U/hcOKro6ekpSYzaKgqwO05r5KyFzUZ96Q7ZH3lARvD9Ec/yguMF09WUmoVOJb+WJva8xwSXXgd8F553uWfL96wnmrdLttnmrOYS9Zp1E5SAE+ejJGJ4kcpg0KBL72denX3t7SPcefvfKywaaHn+qY4JBBjuCK5obNgwWEUoX0hgCM3YtalOmY5aGlqdW0PruDx6vS995P6jT3NwDLDk0bOiWJMPc9NEf6UHxa2mCbaUZwCHVPeGV85XxaebB79XRLdQtwnWmjY/Jbs1EgSOk+9DQiKYIbgxBvBMr4A+po3hjUtMhJvzG2AapnosyZkJMXkN6K14XNhTOEmoLYhJqJEo1tkfiaDKBDqLWvKLtRw1DStN4p6aL3KgAkDtoYxCQDM7U8r0O+T31YLWDPZ55sfXPidjl4wXvYekl6GnnNdrBwlmwlZplfIVLAS3RBhzVVKuobxROZBWP4N+9d4IDVdsy5wEa0oax2oyecY5MfkS2JYIXohm6E+4DphNWIpIuTkJKZ26CCqJWvUboyxQLQIt035yT0QgA1DLUWhSQJMrY7WUX/Tl1ZcmG5Zfhtc3N5d316PXt2eph5PHq/dZJwUWtqZAFfJVUqTYtCODchLhQgQhbhBiD9u+0K5ZPX7cnvw1623K68o5Gd2ZWOjkmMKYfBhF2GR4PNhpKIT4/SkKKWlZ4TpNqyXLhFwSXOtddG5CPzAf2UCLMWNCMrKyA340LRTTxZ8l+WZ85s4XE8dhx5BHy9etB7hHnJdXxx4WtsZ8RgRVWUTHtD+zdULUckDhhnCmf+JfAx4d7Xt83mwci5f60OpZ+dA5VwkDGNVYY3hSOFMIUWhzuJ6YuxjwGXTp59orCsE7ULweXLgtft44fv6PhnCS8USCHxLYw3gEPHSLBSmVwaZJJtZHURdVp4OXpKfEV8oXpTeOdw2mysaDtg/1goTudEHDqPMfIj+Bf6CfL+k/JM5j/ap8/7wnC6lq9hqK6eJ5nLkMuK7YlehRuFIYXPg9uFqInakd2VYppxokustrUZwAPLctYx34/uovkpBugSjB6yKCo2NEFJSvdSf10vZBNs63GtdeR4EXx/fO55SnptdtxzpG5xZ+hetVlbTsVH3zxVMDYlLxfqDBkAS/NR6Djc99HXxsu3ibBzp9+d5phSkziO64rQhQGDmoPshLWHyokWjxSV3prGob2r6LE8vXDJBNSh3GDtgfgDBK8QohyAJwI04T2SSBdU61rgYiFpPHCydKF5q3mdfLN5CXm0dupy+mqVZlZih1pKUUZI7Dw8MwIm2BlMD2kDefWR6YvdhNGCxwG/x7KCpzWgSZwQk3ONfIx5hxiDEIQ1hUiGO4qhj2SUxpoooqeqYLKlvEzGcNHs3H7q3/ZQApkO6BkYKU8zeD6tR4lS7FrKY+Zq5273deJ4uXqmfB580HoreLl052wPalll7VnJUv9IPD2HM9Qokx28EA4Fpfd+7LDe9dN7yrq9g7NXqzGhcptck2GOcYrmh1qEVoNrgsmGzYcOjauSt5nWoP6nH7FpvqbIQdD425LrbPR1AooPvBlsJoAvizwDRupQVlnaYI5mUW3Kdvd5lHi1ewl8JXkZd950sm6sae5j5lwPUzRIHEFQM5EpBR/1EvEGa/ly66LgeNKgzMy+VrSTqGahBJyQkwOPHIk3iRCH4YKdgxqFMYpWjhCQRZjfnV6nN7ETuYzEodGx2nrnmPTb/7kKyhlfJPAvGTqvRVhPHFZgYQlmDm9bc254i3r6es976nvveHF1+G9Da+pkuFx/VkpKo0L0NfoqSh+fFBkIgvtz7kPhX9jDzlPC7rRnrIKl7JrOlYeRa4sjh2WFf4ZRhAOF8YdnjI+PlZTdm92kqK2xuAHDWMxm2x3o4fHb/UkJrBaiIqMugTjQQ3tNoVXBX99mXmvqcrN1R3naetl8eXgieH12E3FdbfVmKmDWVN1L2kI2ORAs4CEwFfkIkv4N8Ofk7NiS0GjCSLhQr4OoMp1tl/OQnYu+h56FT4WDhPuF0IitinOQxpRsnDWkjK1vt3m/ccx51mDmqe4X+x4HUBM6IWIrczUFQjdL7FYSXN1kfmrjcot1k3dbep57UntSeT52oXNvbt9nTF/hWPVLi0MUOhYvqCNSF/YJrP9E8uLmmdlLzVbFcbbisL6lzZ59lu6SpIs0itGE1oWthLaHlYjBiu+QFJbsnkujNKzgtpK+hMx21nDgKu47+v0EChI3H7wsNjgVQmZLv1O3WgJjsmpHcP5ztnjleF5813wqetd3hXEZbT1p+16EWSVPUkZ6Omwy0yV2FqgLLv/m9XbmbNvF0MfEN78CsTam66APmxaR6Y31h6uFCoMPhrGGwoi+iRWP2pSCm02kJqovtcm/oMpD1Q/gM+1L+ZsEtBD+HSopajQAQA9JOVPMWm9kF2ukcKxyr3lSeYJ64nqWeyB4kHQgbrZpEWIaWdVQuEYrO3YyTCadG8sO5wTn9pbqut++0vrHyrx2tEiqm6EtmteVS5ARiQaHj4PUhguDjoWBiACNDJPjmo2h5akPs4G7TsZg0sjdvOiM+OgDpgyQGtklLjYTPZxGBlLfW3hiq2rmb1ZyDnccet1653sEedJ3pHPxb2VnuWJrWilR+EbHPeQxFSfOGggRbQMi+Mvqu96y04DH/L4ztb+oyp8NmleT7I1uiqyGv4Wgg++CuoYGhyuObZM1mUKg36mRsMS5ocZt0gzdnOUl9mQAuw1RGH8ksjAbPOhG5E+aWiJf+WkBbbBzBXi1eT16EXyAeyh4BXUjccdq3mPQW5pTH0pjQX00DStSHlkUMQf1+xbsy+DT1BjJoL0vs3erWqMlmk6U+o8kjDWIdoVEg4CFmIbyiM2Mq5GbloWffKhEsES7EcXn0Bjbi+Rh80X/jQw1FlMknC4zO71DDlC6V7FfsmjZbYdwA3iLelZ6onute7p3eXZ7c7JrnWZHXFNUXUrmQOo2LiuZIB4Vuwa1+/TuMuQy2JfMgcHutMKsxqLQnSOV6I++jBqJe4bmgieEO4ZohjyNypB/l6eeNqYTsPW6wsT70Hfaa+Yh8gz8mQaKFsojlS0SOXtEnk02V71d7GdnbblwfXW/ebl6LHwsez96j3hQcvZr72YPXglWhEsUQsQ3PiwrIaQVlwcS/RnwseXK2Y7NL8I+tnisy6bgnKGXOI70icOGeYmShIGE/IXchrqMjZBdlvCexqbBrHu3EsNazNzX7uLd8DD8ogo6FNgfwSydN8ZDwUwzVtNbgGZIblly/3VCeAN4V3xGexZ7z3VScnhuCWlPXgpY7k0QQ9A6yyzCIoYYgQq+/SzwOOWy2Q7RYsLgt/eufKflnMiZ9pAdjgyHOYR1hnOBOITGh9WLXZBOlmacX6X+q5a1uMDzycLYrOI375v84giFEa8e9CpcNtI/xE5MVNZbAWUba2JubHYWdw16sXxQfR163HYRcx9tNGfQX2dXIlAGRGY5XC2gISUZIQ7GAn/yXulB2zXQt8O6tzOwI6cBoNaWdpEfjOiIvoRLg1WD9YOHh1CIGZEalNKbAKNJqwezzb+xyaTTZuF372D5lAPMEckbKCroM08/gUorVGVb02DpZ3RutHJAeK14THlYemN7NHeNdQpxkWpBY3NaOlApRiw7gjGtJTwaWRDG/+313emP3UnQX8Q7vIqw26glocqauJJ2jPeJiYZBhJGDp4WPhKyIjo/mkfqY+qJpqNGyhb0LyDjTzN5t66H49gNyDTgbmSWZNCk+K0fFUMRYi2QwabtuC3aTeDp6fnx2fNh6TXilcwFxSmipZYVcY1JTR20/gjWhKiodxhAVBQf3Vuwy3HnTXclbviSy6qYAoUeaFpMGj5+KW4a+hHqEkoQBh+eI8I01kiyYl5+/qXKwRLw1x3DSc90V6nP3AQJ1DjQZQSdWMWo7E0UzUu9ZxmAyaGNs4XP7dfF6i3oBfLR6Nnn+c+xumWqkZOhefFNrSZo8RjSKKPcb/RFpBi/6DOwn3//Tscmdvoqyk6ruos6anZQEkZKKTogyh5mD9oRrhLKH2Iq7kaqY/p78p/Wx5LtJxJnQVtl75Sv29AA+C4AWNSXOMeQ8ZkWVUG9Yi2EKaHpu+XMHdyp5cny7en570nf7ddRxT23cZYRb1VRDS/xArTXSKrkfUBNzBlX6f+7x483WF8v6wNG0A6zYpD2bMpVyjwCJjInvhAaEMYVYifWHv4zhjraWk58Go4mvh7hWxAjPxtqP5xbx5/w2ChQV3iAELkI5ZEErT45X8V3YZXVsQ3JpdL54XHyuesJ6InnZdmtypmlMZNRf21R2TbdBHTgVLTMhSxS1CMP8wfHG5B/Yo83IwQC3jaytpEGepJaZkc2L4YhagwmERYQfhxuI8ot4kDyV0ZyzpMir/bjZwr3MT9Yb5WrwQPwqBwsVUCCnLOw1iUVAT+ZWsVpPY19uM3BYd6R5nXnNeoV7DHpQduRxWW2iZTpiC1f/SydEyji2LS4jYxUUCMn7G/NV5DjahM20wM65/q0QpdWfiJbxjl+MFokMhluEUoX/hTOHcIqRjxqWaZ2qo6eqX7PzvyHKI9k/4UzxX/0bBg4UOR/5Kw036D+oSpFUc1xjY7RrtHDgc+l1HnsMe117Y31od01zX3AiaQZhoVn0ThpGtzp2Lg0kRxmqC3z/6PKD5+Pa3NEwxm65B7Gyp72dxpkskZKLfIj3hDmEO4YYg0yGyostj1CWl5u5overvLVswEnKQdQz4YbsYfi3A/YSUB8VLCs2tj/1SndTNV6jY1tpZXCFdNJ5zXqyfCN9KXyEdhl1vW4SaWdfulovUJpFCjzxMuQkRBo3Dw0CUvSS6uPaDNKkxVS9VrAzqrOgVpr/kdOON4gqhSiDbYWhgruGoogKj56VK5ypoMOrXbOUvN3IUNJ/3pTq8fVrAnYQwRuLJiQzQT3gRrtTDFy4Yk1qJ3Duc2F3y3kkfHZ90XkCeFZxwXPJaOxjAFyCUfNGQj6VMtcnuBm4EGADlPaA6XjbY9G8x928VrS9qoygK5mNlKyP54jdibKI6ITwhQGJH4pVj6yTm5ulokKqKbEbvjvG6dGU3XLpnPUTAHoOwBnGJrUxeT7MR91PDFpWYttow209d5F463oKfP55r3lAep50PXJ2a5FkM1wLVStK+z/oNJEpAR+TEoUDI/hz7ebfENYCyMS+87PAqRGhvpkzl3KOKYq0hT2GoITng+GG0IjQjM2T/JfWn/alwrBLutfFhNBz2ivpb/VpAAgLhxlgJeUuYD28RXBPlVrgYSNpV27Pcrd4vHmRfM55znlhevd0N3Fsbc5j/1z2VvBJG0BJNQksNB6cE1wHN/pe7jDhTNX4ybu/bbgXrXmkWp1qlcCPYYudiJiGeYV6hOGG4YfyiUySJZeuntKnB7HguALD2NBB2mfmxfPq/fcJlBaoIjkupTebQ9ZNh1b0XbdkKGv/cU92HXmDeip7k3sOeOV3ynGKbHxmUF/pVRRMkUL5OIorGCJSFeoHiPr87pHkKtkLzPfBl7igq62m8Zt4lLKRMIvLirSFu4KAhC6FoocNjBCPJ5mln56j367guYrD3tAN14Pjre8f+wEInhSYIlAtEToARgNM4VfYXLhj/mwRcxN1G3oleY58P3zheOR0OnH4awBm+V7jWMNLCkVcNhwvGCJDFL8Iyv6S8Sfl0dTSzUnEbLqpr32kwJxkmJ+OKo3Qhh2GKoXshK6GQ4fuitmR3ZaRndKjfa+WtqjDOcmk1Grk1O7O/HQH0BO1IOcqVjYxQgpNJ1bGXu1i7GqdcuZ1x3jCeqt82nwIecN6nXJ7bPFmG19TWAdP0EU3Oo0vsCOrFyMKO/2X9PnmE9y2z7PD1bjKsK6lp55dma2Qg44ri3iGz4d7hLeGhIU/i5GO+pW3m4Si/atTtYW+Q8mK1r3iae2s+OQF1hGhHi0pujadPlFKFFQ2WtZhQGxscYhzJ3iUe6594XpteV911HO+brtoc2FYWRxQ1kdvO40wDySZG6YN0wHP8wzpXd1w0HvCfrgYsa+pMJ6JmDaQX41hic6F0YWAhGyCbobEinaN1ZKVmAOhRKqEsym+Jsw/0uzdAu3T+ZkCjxHUHHgotTGPP4tIdVMdXDFk5msKc750m3fTegx6TXyQeOV6aXNeb1ppU2M/WnxSUEjCPSAxfSXbHRQQBwHS9eTrqd+D0ozGvMBlsQaooqF7mvOR+o0vidmElISnhH+FEYhvh92MjpLgmJagpKguseq7/Mj60BLdTenu850CHA6SG8MkWzM6Pp5HYFCDWZBhS2jRbg51dXfhedN8mX7LekJ4XHSicF1sGGTsW5NQUEp5PhI0YSnOHWQTVgNJ+qrrjd4I1QvK8b4Bso6q86FZmp6UZo6Qi8yHV4WOhSqEYofaifKL7pSJmNGfa6k2sfe6ucT/zrXcuue59GD+aw61F4gmdC8EO+FFQlC3VQ5im2cAcU12zXZ6er96unsUe3x5WXVtcL9qtmLIWvFUcUpGQW41KSrAG30RfQRu+lnsZOLD1QLL68AGt/isuqGQms2VAY//ilCIHIVGhSiDcYaRiQCNA5KhlSyfW6dlr9y4qMMUzaPZC+WQ78v/rQmfFSQkdzDQPdJCvE+RV/tfdmkQbeRuGnfTeNB7rnyieWB3hnTtcI1q8GRsXG1Vmky4QY836yk5H+cRdwiT+zXwSeSn1UbMxMJxuE2sFqY6m/aXwZAJjDSJfYZ4hBmEvYU9iOGMf5H0lWedqqYpsXK6q8HPzdvY9eQW8R785ggGFQYiEC6tOCtEoE36V/Fe92f+brt1S3XeeaV8bXk4emJ7RXeRcZRrAGaiXr9WV05AQyk4GS7NIaMVmguBAFbyleV32MrQ6MFpuSuvtKgenNyVaY+mi+SHUIXqg/SD+oW9iFyJhI+al8mcpKOZrku3g8A6zI/X5t/S7pL64wcJFT4gfSwBN3xAuEuMVlJfE2UobbhxPHX1erZ5AnwPegh6n3eAc9dsc2fMYgpWXU8ZRhw7Ni4bIzcYPgs4AB7zmua22hrOEMNGuCmwGaYan7CZX5OEj2OJsoWGgzaFVIOjiEaKn4/rkzya76JDrTm1r78Ly4DVTOKZ7hL5Kwb7D9gbmigqM6FAVEoBU19aYGTmauxu33apeDh6o3rneSl5OXccdwJv12Z9YLNYJlB5Rj09hTEeIxcZJg0LAHH19ej/3bvR3cZluMKxfqk4ooyZ6ZMUjYqJqoZfhBKEEoV2iOmKOpCdljOaLqP3qzi0jL0xyDTTt+C46eD2KAf9EZ0dPykhNbk/QUqxUk9bo2IJaBlx6XJNd4l7OH1le9d5KHZ0dHVwtmjgYPRboVF1Rco8TTN5JcoavA5oAk74SuyU3Q7Uuse5uhCyPageoKqaxZOljTCLIohfhIODfoQ8hpaJdotZk3yaOKIqqQKvzr6hxgjTyN7C5u71nQLeENsbpSl4NFU7wkkTUfFZ0WAeaGRwcnD/d0Z3I3rXej15F3kcdT9wLGlcZN9aAVN7Sm08xjMsKEwdSA8DBMv38uqf4EHVBsp5vWC0lqnjoBScD5P0jvWK9YkFhMGBJINng3+JTI2blCyYk57EqMaxH7laxRjRz9xM5+rzav/iDOMXeiapLZY8wEV4UMNaRGCTaLptK3MZeH15+nmueth6snakd+dvDWt9Y0lbL1HnS0JCjDUUKi4b2BCoBKv5OuzB4hfUB8oSwRS0S6pqpNqbSJc6jhGKpIaFhRKCp4UWibqJPIwukkeY0J5FqWawprqQwu/N19kr5HPy5f+CCpUYryLqLh46TUXtTvJXql+QZottznJ2d393BXyPfHh7VXlrdSxxjmwzZSldoFUCTGFCQDhJLQAivBSQB4f7CfIz5BrXJMwRwl22mKuQphOcVJb5kCaL74m6g8iCVoIDhVSH24zXkEuWQJtVpjauOLgkwRrOHdga5MHyOfwJCPkUtyK8Lac4JkSaTGJWMmA9Z3dsF3IVddV3GnvgeoR+gHpHd/du2Wu/aJVeolb6TLVAUzkTLkkhshV0B8n8GPBM5S/ZV81ww6m2p68EpZubG5bGkfyLdIlthcuCiYZRhhmJ2YoPkMaVRJwepWyu8bgBwejMO9eq4+Du0/uyB5IUcR9SLSI4EEPRS6hVHVztZdVr2nFwdAd8XHnqfYd6eXghdrtxOG49Z4lfr1dBTypDhTpMLFkkqhchC1oBi/Kr6Izab88fw6a5zK8zplWfbZYskS+MK4g7hgqEkoN8hWuHBoslkH+SEp1QowKparTAvU/IXtUB4iPvCPlrCF0Vdh3QKRA2K0F7SpBV5F0vZTNqt28XdQl6DXsbfMV7+Ht8dwV3lm2saF9ifFWOUrNGXTsKMksmkBh9EOsB/PMf6UjcoNH0w0662bAyp96emJh0k2COpYqShNCDDoV1hnaGrYuCj6iT3Ju+ogSsX7QivC7KkdTx4JfqePcyBFYQHxwPKm4yWT/KRpVTLFscZDppEG85dQJ4cXoBe3N6i3oKeGJy/G16aNdglVjjUBxHBTzMM+glvBmIDvoCS/fM6ODcVNCpx7K707Cmp/GbFZmNk0uQGIlVhgiFUoLOhCGHLYiqkA2SWpo+nkyqm7Otu2jIodHU3aDoMfXVA0MPNhv1J8wwoDw5SKxQAV4pYulp+29QdHp3DXqne/J8dnn0dWV2hnAJa5dlDVuhURhIcj20NJMn7Bz7EBIGEvfc6kPgCNI3xmG+qbS5qnGhUJork8yNKYpKh2uEaIYYhHWHb4knjoyStpfIn+KoM7JavRzFgtEW3YTozPQvA4gNPhn9JWourDkNR29QQlr+Ycto3G2jcgh2pHl5fLV8n3y/d5dzaXAUatxj7Vr7UhJL60F+NgktOR13EqsEwPmA7wfh09ERypHAOLPaqw6hMZv9lXiQ9opoiBeGCIMOhFOGZomdi4WRWpiCoHGoDbG4uhrGYs8V2ozmOvVn/30MXRkEI8EtvDr6QaRNQFbvXxBnEGt6dSZ233tdenV6dny9d9l193AMbNJlrFxgVNRKDj74Nrwshx8nFGcIkvqL7ZXhY9iByyTAIbaQrD6lpJ3zlO6Pb4v1hWSGWYMLhoCFoYYGjfCPm5XbnmGmk60QtR7D8c4D2nTkCPFf/t4IHhe0I1gtwzg3QzVPZFVaXuRllmuzcE12GHkKfn16HXr4d+93JHPmbWBnnV4uVaFNrUK4NZ8sayBuE7gIH/3z8ArlcNp5y6LDRblgrSylBJ8glduPd4snhzOIAoNTguqGQogFiv+O+pUfnN6jHK4VuLLCAsyL2h7i6u/H+zgIvRYJIn4r9TV9QdBLGVUpXtJmVmwycj92YHmReyh8m3rOebh1k3SNbpNmz186WKFNekRXOd4tiyJ9GcgL4/2n8pPmltrez37B5rhsrnqlk5/qlRuSvY3shRSGwYXFguGEk4Y8i2uNiZWYm6ajjqz+tUC/gcrd1SfhrO6J92kFfxMeHy8tqjQKQ/tK4VQ/XpNlpGwfbqBzzXm6fcN8k3txe/h31XCNbfVn2mJ7WMBNVUXgOz0wtCTvFfoLwv8h9uDmg9pz0crFdroNsh+o2Z+2l7SPxIzkh76GcoVMhdeEjIi/iQaPB5Owm8uhYKoFtGO9jcZU1Zjh6+uZ94oFkBH+HZApETJiP+hIVVXgWt9ki2vGbzF0snejekZ8sXsAesh2ZHKMbuloF2N7W31RlkYmPnox1iWUGwEQ2wON9sHo991j0RnHr7v3siKpg6DMl7WULozziMyGtYUZg++GI4X7ihiPmJFtmXmhRqp/slG8HMbX08TgQusq9oMDXA8wGWsp4jNyPxFJTlA6W7lj9Gk3cM5zgnfdett7KnsdeuJ3hXPobkVplWHNWopQhEgHP5ExPylrG5cOqgQR+Rfrdd5p07fJ7r3HtLyqT6PmmROWto4UimeIN4a6hl6GUoUoiViOupPumSefDql3suS8k8ie0vDbIuhH9hwBaw5lGZIkizGxPCtHS1HlWVliLGkLbf1zDnmPeix70Xx7emh5dHUMcWZsZGRkXnBTXUpNPkA07ygaHfgR8gV3+ZDp/+Ft0yHIyboKtW+s+KEjm6OUJ4+tiSGJUoabhNyEAoZziJaNQZP+lT2diqdnsIS5/sOTz+vdKenY8kj/CgxFF8YlPS/pOg9GFE7dVvJg5GXMbcp0kXfeeX5633n8e8V4/nNKceRqQ2WnXYpVKUycQtM2LSztHbYTvAa1+lTvFuSe1nDN9L1ps5etyKLUmjyW2JDRiQ+H7YMehGeEkIZOiZKKPJCmlQyf/qVzr5W5XsMHzzzYJuf08zT7HAsBF3Qibi4rO7xERk/zV1ZgFWfBbHd0xHnAeAR6hX0Ce0V4iHU+ch5sXGeWXu5Sxk7DQgo5aC/qI0UV+we7/f7sF+IS14bOX8JItwOvEqQcnP6VMI4yiyKIxYRMhC2DdYSYhs+LmZHzlmmbv6U4rR22I8S+zL7ZDuRf8K38Ig3pFAAipC6MN2JDsEwbVqxcBmZFatZvwXcUeMp7o3vtetd4UHeocFJsnmZBX7tW7EsMQ1g6By3DIlAWpgp6/wDz1ujc29zMQMWGuXeucKbqnSCXCZCJjOCIkYXBg9WDjoVDh4+KwZKnlged2KXPrNm2X7+ayj3Xy+Hi7mr5XgkwEeQfFSoxNlNBLUhFVE1dz2XPac9vfXdgeEd7s3z1ep96Z3h7cs1vIGZ2Xx1X2E9sRO06ii43JQ0YlQtOAA/youbs3G/OYMGnuJCzaqkHoH6W249+ir+IAIjWhHWCf4MYiC6MX49VlNGdnqPOqfy0Q8FvyVvWIeFc7eT4zwU+E9wcWCj3NTw/bUurUvVbP2MCafBtBHXVesx5jXuUfXd3B3c8cZZvLGacYupacFA3SaA8hTIZJfIabw28AP/z9+da3mfS58bXuZywPadsnnOZHpIpjD6I/oW/hLKFCoNXh6CIi46jld2aRKFxq6a1i7rYx9bTK93q6LX2AwW6D4EckioSMr49J0cdUmJa9mJ3aOpwMnL5d3V6BHpsell6iXnqdYJvkmnQYCtbslHnSug9njLxKMAasg95Bez4eOzb3unTr8a+vM2z7qpDomKXdpIgjI6Jf4iEhvCCloTzhsiJiI1KlBmZk5/Hpu6y2rwkx6vTudw96jn0jAMFDlgYUyYVMDI7ikUuUMtZ6F9xaAlwV3QSdyV71nyLfWt8Xnj3dD1vpGl8Yy9a0FL/Se4/KzUqK58elREdB134kew34l3U+Misv161vav3o1Obn5b9jxiMTYhqh36FZoT0hPKG1or/kqWYSZ8fqbqtfrgrxfnR9to15uP25P4SDWMYECVvMVw86kaoTW1ZNGLpaI1tInLWdHl55Xs6e1V5CHn3deRvmGx5ZFZbFFMlS/hCPThNKwogJhQNBvL5O+2R4gjX1MuTv2+2WKpVotWbR5Qaj0qKvIllhGiEIIURhqKJ442ukCSZ/55rpfuuArjNxJHNPtnz4w3u6/8kC5YXOCORLSg6lEXwTTBXt2AfaSxu3XKId9l6T3qSfE18uHkWdKlzj2xfZtpfdlaDS2tBPza8Lp8hwRSACWz90vAV5Eja1MsowR24RqzOo66e75WPjQeMZoadhQCF5IXdhFGHwoomkg+XxZ4Ypo6uMbYvxMrM+9ct5L7wo/1oCtcYsCBqLQ45w0Q4TSxV714zZ45sXW8nddB3zHsJfIl8tHxodcNyoW21ZaBeYlc/TAdDBzvrKwUjSRZ+CY7/AvPU5n/YXc4JxHe4qq36pE2dApa0kYWNnYg5hNiG8YT9g1CFmop7jmqW7ZyKpIeuhbd0wMHLXNa64hzvYvq4CBsVwh49Ko43+z92TEBUPFv8ZOhrpXBFdhV51nkjeYl66nhEdZ5ytW4PaMBdXVprTlxEYTlPMp4l+xdSCy8AUPQN50DZG9CsxMa4n64jphOeNpjpkfGKLIknhhyFaIO5hGyHuYz5ja6TqpvqpByqRLVHvz/It9Mm4ontSPvyA8US1x2zKM00LkFPSNNRqlyEZcVsQHA0dhp4TXoveqp853gOd9p1VW+UaLFgNlmpUNRE5zxFMy4nzxgvDO8BK/Tu6fzcptKaxAG9urF+qa2f8ppOkZiMrYi0hhqEd4U2hsiHOIlHj9SSOJoYo5qp+rHCvUXJItQX3yzrQfeUAz8O5Bv9JpMz3D+uSJFRb1rqYQFqG3LidJt4FnrBe0l82nm8dUR1UW8taNBkllhKVBtJhTxOMiop2xttDvwExPdr6X/hWtJqx7y96LKOqi+hz5jokpuOZ4uRh/mEF4PqhO+F1oq+jRmTOpl9njGlebOTvAHIFtJq3cfoRfnRAcEP8BtTJtIxjjsxR7RP8VnrYxRrdm/JcvN333nyed54yHzRd9x1YW8Fa8VkMFujU8tI3z7NNRoqnRwTEDcDJvcA7Sng89Ihyie+qbMYq+ihnpwTlRqOfomdhreFhIOog/uEL4rVjAOT0pe9nfOnS7FBuy/GWtAP3IHpWvKc/yMOwhkTJFwu7jobRc9PkFbiYcJmy21Ccy938HtCer97L3uFeCp2o3JDbOtjBVx9UpRKXT+FNFYpUR76E6wEDvuL7T/iotTVyZy/3rXaq/2kXJmglCaQFIoRhNeER4UwhUKIn4iXi9WREJm5nfimdLAwulfEDdA02YrmxfE0AQwLPBaHI74vzThNRJ1Pq1fwXzlmh26YdNhz13YRfMZ8ontUeDt0GHAabmxmYF6oVGNLAESENkMsMCFAFcEGRP9m70Dkbdg+znTD+rUrrpukYJtMle2QTowQiauGHoUehd6FjIdOi4aSBpYcnAulKK4MuQfDfM7q2KPjo++u/AUJOBU4IYYsZzg9QqJMUlZ5YCBlp2yRcY91unjPfMt52nnNeVZ2lHFbbC9lxF1XVT1PPUSlOfUrpiO4FCENnv439KPkBttLzhjCd7u7sKulL53vl1eRUI26iUCDHIbmg0eEJImbjFqPapRsnHOjwKuktibBWc0s2Obix+8P+zkIQhUFIbcruTd9QupMiVZmXiNlkWkHdOF1+Hkufdx7BHsYeHd22XLobZRne2DYVs5OdkCjPJAv1iEIGLoKl/5E8wXnnNqlzsDBXLnTrp2nR53jmB6UNo0gh4KDlINog1yFxYbmiW2NZpaPnEmilaynsxq/gMcS17Phe+xQ+jIGgRCzH1EpnDb9PyxMbFKSXcpk1mvEb7l1tHigeil9AXrdeVl3o3YIbZxnHGOxWEtMwUddOjYz/iPnGm0MRQB69HfoYtq3zxbIDL0ksEqpYqBjmGCQ445/iFqDlYRBhR+Fn4aWiU6OCJKUm4Wj8KiAssm938lI0wff+ewv9sYCjQ/AHbwoDTQjPqRJmFA6XBRjiGtlca11Ang8esR6AXzSeUp4cXQMbkFpr2IFWRRR6UfnPQ4zdyc5HZcPLQMY+R/rMtwA01zHn7qbscSp6aEDmHiTEI1+itSGe4SIhJeEl4eQhy2OKZPLmgagtKjxsVi9XslS0Wbd/+jb9sEBoxB0HMYlhzJzPiZGjVHeV/pjkGpccLdz23jAeKN60nohfD53wXQ5b/BqeWLLWuJTqUecPhg0UyrYHNsQFAWh+aHpYuCJ0lHKZrz7s8On0KLem1iVC4+oi7GG8oYChSiGqoSLhxSOz5PLmDOez6edrpG70Mbb0cTdSOaE9LwCuwqGGoAmlzAXPY9E10w4WmhgfGfVbqRz2HZle/x68XwQeVJ6AXTEb3hqOmTSXW5Unkq7QdY18yl5IZkQPgbm+entGeFH1N/LFb6htsGt9KJAm7iVG5CQjTSJQ4XYhW2EM4ckiTWNK5IXl4Oe2aZ+sbu5ncRMzwXcGuWv8Yf+4AvjF+Ik0C+fOzhHtFA2WJFhNWVIbH51Ungyest7LHtIe2h20XXVckNr92UOXzxWSkzTQrM12SzkHyUUwwdr/OXvqeKf1aHM2sLmthKsAqVOmwSV5Y+si5mHT4NUg4iEgIXWh6aMsZF9lw6e0aLSsKK4nsJeztrXseLS8tX8KgpfFVoiki5IOAxClEv1V+xex2aaa6JwaXWQesF8DntBeit553Wkccpp6WVZXX1X9E2RRCk6Ri6HICwXnAsV+5H0xeS02a7ML8NDuF2t9KQdnN+Xw5FAii6HTYYMg5aDrYXbhn6NOJH1lWSdlKT9rI21FsK/yzHXSuIZ8Fn8CQgsFQQhtyykNLxBPU7OVdtcBmWwbeluhXZyeMB4T3yLfCR6R3cyci1tdGY/YldXnk4CRk06OS/+IZkYewvB/mHzd+Xu2WHPCsbauiGvdaVdna6Vx5EHjmyIVoVXhZSEIod1h6SKdY7glRKejqIUrl209L5SyQ3U/98u7Zz8Mgg5EVEdGygON5s/d0qSVO1dD2W1ar9vhneWdwZ4n31UfHR5fXXkc8NwYWh5XnpaqE74Roo8PTKWJ50Y0AybAF/0kOd22x3QDMh4vJOyQKgynwSZ1ZFJkI2Kc4auhjmEa4a7hsuL44+6lVSc3qKzqV2yg7sTy+fTC94g67H48wL7D7EbBii7M+o+qEfCVFZbBWJqaKtu1nJSeR54JXxDeTR6S3nHdSJvL2m3Yq5aSlFyRxg+RzKIKP4aCw4fA7bzjetv3gnS6sT1vpSzqalyoRyaK5SNjEOJZIawhFGDgoUHiDmIDo57kxuZQ6B6qf+yibwaxxPQt9/s6132VAG8ESsZEiYeMnM9q0mMT75cEWHralVv53WQeG96MntLexd55ng4dFlvWGrgYQ1b41XTSaA/kTRSKKseghBYA1f4zOzX4FbT+8hMvTCyEqksoaiahJKUjYeMKoW1hrmDooT/hpaKYI/Pj0KXZ6A0qUOw1buoxcvRAdwh6Z30IALQDGwa1SSFMCM8oUg5UB9XNmGXaCZuNHKsd/J5NXzledx7enn3dRBvfGsGZUZeDlO2SfdA4jN6K8McHhO3Bc/4Gu0T4j3VTMnYvy2266oyou6c35UpjlCJlITphaqDWIX9hhKLBYwlkh+Vj58rp5KvnrpNxaDQAdwL6Bfzav3nC1YXpCJdLuA4q0RYTtJZ8151ZwFvjnOvdjh6yHoSell6dXiUdMNyw2tSZQhfa1VOTFNB3TWtLC4g9RIbBpf5du/P4ZrVCM2hwD62tK0cpkedfJQDkDCJTYfVhr+GRoO7hV+GAozRjuCVdZwVpXGurLn9wh3P39qN5kPyf/sECEcVFSIwL/M5+kItTWNXaGBHZ6Bq7XE4dkV6TXxge9d6HHkoeHFzqWzSZI1dT1dpTThEKTjwLdQijRYFCTn8Yu8P4UnZhcumwgy3la5BpkyefpfEj1OK3IkuhTeD7YQchgyHG4tbjdeWEJwPqJKu/LYUv+XMz9e548DwAvspB9UV5h+ALC43WkPUTW1XCl3gZP5swnIZdfl40XiRezd8AHlNeFh0U26lZ0Ze1FY9TwpGijhaLfIhjBYOC+b8nfIh5YDac82exIG3hrDApDafx5Z1kXWKXIrxhymFpYOfhR6HtIv5kL6V0pmnpXernbfUwDLM4tZu4iHvSvsZBIkSiR2VKik2uT5qTKhVaVy0YydrHHLidb53RHsUfWN7oXrBdoFy8W3cZ1tiAFmhTzNHtztlMNolJhoyC/QAdPK55sXaoNHpxPO5MLEFqbif3ZhVlIKMdIiNhQyGD4R2hNyHPo1Ojc2S25rIpOqpn7Njv+HKqNMT5EbuPPnnAsMQTB78Ka01/j4jScJTDlvgZZlqO2+TdAt49Xs3exN6t3kke/1yyW1xaAhl0Vg1UotE4DuPLpIlUhvtDWUCs/W16ezdhtFFyOW6JrLipzigY5itktiMiYoKhqSEuoMehY+FCIpej3CTEJuloVep6LSBu33GtNSo3TrrSvZCBV4PGxrTKJEzsj5pSB5RUVxUYxRqeW7ec2945Xp6fBJ8YHt9eC510HHUaXJiBFryUnBJvz0rMpEnfRswEpkDFfdB65neOtUuyKm+0LZBqweiRJ4yk0SQDIi4hyOEPoOYh9GHy4gmjbWT+ZdfoGSnFrApu0PFcc5w3TbnVPMSACwPlRhRJPsxpTwoRt9PiFlfYGBnzm1Acux3F3vJenp7gnoReUd37m9Wagtinlu+Vl5JB0EsNtkoFx5hErQIZfaD7IXhHtSxy3+9GbWhqXWilJuZlQiONYjYhSOERIcDg1aFQ4Y2jKiSqpjIoDinabAzukTGZs/c21LmHvPm/YANfRSUJNYvBDzhQ7VQYFm4Yepow21Jc+d1WHoAeyp9gHvId0h2KHJRaqdmnF0oVsNM1D8vNQsrnxssE/IHYPt17Urk2dVOzDy/r7b3q12kwpyJlIWOkos7iMmF+IY5hW6EGooRjiCQUJXPnCmmyK1puJzCxsut2MLmrfG2/1oKtxcDI5kvZTnUQzhNxlgsYEBok2zScy55RXume0p64Hp8eyd1pHKXbWNoel6RVGNOKURsN4wsHSFyFWkJKPtk8R/jadgGzR3E07l+rGumYZxhmAORTY3liBeF74MEhZSF1oeljEiQ2ZXLm1qmqa2euBHB5s1s2GLijvGu/HUJNBRrIacryjYXQnVM61TmX8hlT2upcF117ngQejV7J3ojej53UXJObqBjd1/nVrdNzETDOtovziKKGPEJqP2M8B7no9gDzj/Eybg2sLKoH581lj6Q5o2ZhmuCgoPrhR2GCIgJi3+M2pRandqiH62ItTDC/sqO1Tfiou6r/MIFMhGpIOkp6TjZQmRLzFMsXI9lQmvcb750HXgQei58XnzveY54EHPubFVn0WH9V21QV0R2Ohgx8SVpGVcLNgF18cjnQN6yzRDFsrsFsbinxp4MmDmRUIwciUmFzoTghDeFjoXDiYiPG5Mjm3KjWKwXtA+9Ecm91fXdiO1C+FIFpxPKHNUpfDRvP9hKVlJlXCZih2s2b1Z1WHjMehN5qXumeAF47nQobx9o7F8HW8ZRmEY6PMEvhiSuGyEO0wHo91fnLNwa0+/Gu71RsLqoRaJ2mmqVZ48sirKGxYe+gXmFSYkkiVON0pGcmWmiqamwtIO5Y8bK0sHfueoV9+8Cfw9HGgMmoTDiPMtHB1KYWipfS2nCbcx0U3iledd7H3tqfIx4yHNTcG1rNmMDWitSbkZcPww1fyVfGy8R3gOy9/PrdN7q0XvHxbzNsw+qEqBXmgOVU47diFyHA4d8g/+GEIgZinWPIJQlmcagNKizsJq72MQ00Zbe7ehE91ECog8PGy4n+TMGPXJKD08TWmljHmq2b4x0Q3goepd87HkLfKV3eXRZc55qB2OjWiVT9EiiQYQzDCqYHbISuQJz+hDt8d+D1n7JG78dtXKq9qPOmTaUcovdi3mHfYOHhMaCX4RLiPyKx5JmlqWg46Vwrwq6vsXvzqbcveXO9XoCQQyIGBwlTzDVOiRFCU6CWjpdoGdwa010LXheeXJ61nxueRR513XYcB5sbmP7XMlUO0pSQMs2ri1NIpsS0QcT+6TuXeNd1sLMsL8uuOyri6NAnFiVepJEi72HzYZuhfSEZoeLiYCNf44XmTWeYadsr2m6esJWzy3ZLOS88Sz+7wbFFzYjOC7qN3BFY01bVghgh2gZbuFwuXZ5e814BXuxell563N3cQlslmSgXdRV+0uGQXw26SxKIRMV5Aee/lHuTuOE12zNOsE/tgmuXKXEm9aWWJKUjIOJTYYPhjeEqIV7iFmNro0al7ac+6WJsf64McBEzXzYveVn8ev81wcxFoshZSrRNgNEN03iVzteM2YCbYNvxHa6eMt4Z3sHfXh5dnfqcFltSWfvYHBXwkxIQ9k3Yi/aISMXBwmX/xbyROdf2frNjMGiuKewh6UbnX+XKZFgjQKID4YZghqDBoUch7mLHZDblaKbJKVzqxW4NcAGzsnVmeOZ8e33igc7FBUerizENrpBEEwkVWFeL2U8bh5zkncQedB6kHsWezt5inbOckhvf2fwYBxaKE+vQxY6nC4SJRAXOgwDANXz9uZ8267OdMXOupKsiqnUnziY8pDbi86IjIYXg5mEL4RxiPSKnZAlkYibOaM0q+a1mb9ExxHVkuDs7Tj41AXJEb0dZigCNU9ABEr7U91cOWMKbkVwY3XXeO154HyNevh3D3kZcqlwCGkCYAVaMlH+Roc5kTLlIggZywxhAWn0vOqc3yPRjMaZvUG1eqcVn5KZzZNbjaGJPocSha+DXoQiiCyLeI9glFSat6NGrVWyJL12x8HSJN8p7lH1FwRQEkYcZSiPM4U+dkdnUc9bGGIGbAVwtnSsd+N6/HtHeWR6m3i1dgRxgWgNY49dLVBaSHk7GjLEKQcb0w1jBDX1YetF4JXRjslRuWOx66hmoc6ZvpH8jL2KVIauhzyFX4Wmh5KN0I4VkDaYfaCiq0Gxc7sIx6PP1d5L6yv2dgGGDaQaNiTXMfg8LkaFUOlYqmGjaK1uunNneUx2oHyXfit8VXdPdPRtw2r/YxRZeFHMTfE/6DRYKiIcvBC5BeP5/Op731/VWsgcv7qyEKw7oWicOJU6kEuJhoakhyaEe4OehA6JgI95kliXT6KDpvuxErzsxFjT8dpb6HLy7QKICqMZeCVOMro7wUdPUMlZKmGmZvVtpHOBdLd5G3yJeSJ773WQd/FxP2plZCVdIFSASklBTTaTKh0evxDVBUj5/u2T3yjTjMl/vqu2JKzpop+cdZWUjo6MeYa0h7qGtINehTeI4YhNkheXVp2zpkyxE7lyxYXOGtt15Uzxbf0mClgXTCOhLWA5qUQUTpZXnl8LaKdrbnK+dQF5wXsDfHR7xnkedfRxkmqdZuNcUFaZTflA2zflLdUgHBVtBjX7OO8y5kLZuMsaw1C4zaynpnmbH5RPkTSJhIn1hSyFMYVchWKKTov2kDmX1J31pZis5bcewsTNH9km5SXwY/wtCcoWQB90LdM3MUP2THpW1V3jZjJux3DYdQl5PXwAehZ8gnhQdn9yFGshZ+leulb0TU5DqTkNL8QjThceCqr8VPE34+bZv8ypwSO43LArqNOenJcXkWmL3YdMhSyFKYIvheaI54rtj36Vr5wipA2strbpwNPME9ZH4z/vVPp4CNESSB0WK+4z90HkSFBVbVwWZSBsfG/gdYJ523kTerd8rnubeW9zgm1faAFfOVfoT1ZF/jpiLikj4BjwDeD/j/Oz5jPb5s6Ow367EbEZpnOeHJj8kBmOsIm7hbqFeYMshbaHiYuOjViVmZuhpF6rj7RavibMetMR4PrtsvfKAlsTVyD8KQo0kEFJSz5UNlzjYlxqXXDXdKZ3sXvAe9x71XkUd0pyKG7ZZjhhe1juT3lGIz7pMGEkthl0DRUAA/Uj6LDbi9N6xuK5cbMUqK6ep5hBlNqNtIoshYqE3oQNhSyIaIn5j2OTH5dqn1+pxrUmwczHc9It4JfqKPgzBG0Q8RwfKOcwRT+XSPRSNFt+YwRpHHAndfN4gXpUfSd8gnnddQd11mwAaURiR1qQU9lF3jzCMuwnrhzTD/gCb/cV7Bbf6dJ1yHC+zrT+qGuigZieksuNr4kOiGaFXIc0g92FcYn9i4CTp5jNoVCqr7NNvPXIp9By3mroavTWAuYPtBl4JZowWj50SJtQNFonYiFpqG+XdGF4WHpyexV7NHl4eFpzYXDFam5kbFpZUq9I+z7sMgYoFRsgfNZ6f3mAdKtuQ2faXbxTDkqWPVMwTyD1ERkEu/O46HPXvcv/vniz7ahlnheWXY4FiqWGC4QIhBWHwohEjliTD58lpRay1bwGzMnX4uTY8+wCxQ/kHicuZztFR75TOlxqZ7NsHXW0d/970XxTe8h45XMfb29mN18HVnpJhUHsLkchdhMDByb59ucD2f7MucBas1ao7p6tlVGOuYqIhSmE/YKzhYeH3Iz8lSedT6VbsX+9S8g+1SblUPCnALcQiB4eLew5kEbJU5Rc3mRPazlx0nm5eqZ7kH1bd3J0wm8QaRpf/FPUSHw9EjCmIwQWrgbH9qbo4Nr8zY3BRbN5qDOf8Zc3j2WKkYfQg0CEtofEiDiNK5QLm0Skba9cuTLHYNQK5FXwnP75DFgcZyu4NsJFplAPWmlk92rtcJ92e3npfK95Unj1deps9mg/YfZU1kmVOu4y5iMXFz0Jhvmn7RXeY826w461FarHngWYEZCZiL2EZoUlhDKEFIjHjHCSGponpEisXLqVx0nSa95u7/n+oAyxGlwovDi5QrNPylrfY4NrCnPDdgx6UnrYfPB7HHLvcDJpTGAlWKRMwkJFM5slEhh5CYD6BOux3u/OK8GUuMuoxZ8BmS2QF4zIh/2Dz4TdhWOH6YsHkrOY1KLbq5q2csRd0KXgg+4s/1IL1RstJ4A1ckS8THRXZ2RhbChx63R0elJ5Knweeip1MHCHak9iuljvSs4/PjXNKEga9AgX/N/u0d/s0NXE6baZrS6leJmDkHaNV4czh12DBYRNh9qMCI5OmrmgCq6htejCrdId4VrtePsUCu8Y7ybVM7RA7UlnVhdjCGoNccx21noYfH989HoZdjVvu2tZYshZek1QQUc1JykHGxEL4/1I7tPgddHNxYW6eK/po+mZSpJ/jp+Ih4eegj+E5obtjDGTTZb0odmpaLeiwv3NOd2G7Ar5JQr0FwImezNUP+hKW1YWYOppsXD7dRF5CXt1eyR6SHd+cWBtFmRIW0FNnkR5OB4qtRmuCzr+ze5n4rrVBsZOuUCv5qILnDuU24xGh4iGioKigoWF44qqkiyX0Z0nq7uzdMPSzsXbYOtM+SEHYBcJJPIvfz+FS61VMmQ2aNFvEnVoe9h893vzeWN3NnFfai5iX1xtT29Hlje6KlgdFw+3Adb08+K01bbHYbnirhulC51Yk9qMKYmZhf+EoYOFhhGJr4+sl2GgUKnmtQTEDc5G26Lox/QRA/gTRSNiMPY6Xkw4VCJewGkZbid0IHnveiF+FnufeARzeW0GZtxac1JfRio5FSsiHecTOgIy8jHmkdU0yB68drCmpn2cGpW8jbiK2IVfhIuHNIY9iLOQAZW/nn6plLO6wAPMDNji6Tr20wTnEhgi/C9MPs5JyFTGXh9oim89c094oXqfeyN5RXcYcs5v2WUYXrBSLke0OkEvkR/3EnkD7/Kk57DXFcrbvGKyL6U8nS2TQI7ViEmFe4b2hYWFqIcijSaWtZxNp0m0Gb7IyoHWWOjd96EDkRFfIbotZDuNSgVV817SY/tu23WPeFZ6I3tLfB94AHPcbdJlKl9wVKdJXT45LhgjMxJbBb71w+ba2y7MdL15suylXp89lNiNU4oWhmuEJYTphS6IP4/0lBmeSKZSr7i87MuR1tblJ/L9AFoSHx+8LIU4gUepUuVedGQObtxyenfVewV7NXzId9l0zW5IaR9g81MSSFY+3y8JIvcWDwbP9lvnmtl0zK7BqrbWqCShQJXRkQOMMYO4g/OD74WXiIqNVJNwnAukObATvP3KotKt4mjzzv8KEccccCvKN+hFY1FSW3JkH3Dfc0p1YX2vex57MHfcdQ9vImhDXRNWr0g1P5oxXiWLFuUHefkC67fcYM0SwBu12Kl9n1eZI498ileH5YP7g9GFoogDjb6R85nRpXSs5LnhxrPUi+Vg82gATA9BG0kq9DcVRDxPOVtUYsZrzXQHdzB7+XnTfI55PXYeb9JmPGGFVTxMrj60M4oiZBjgB6n6HOsk3MPPp8JXttSsq6E2mD6SwYsoiLCCIYR0hOWIQY2AkqGaZqIErbC6ZsQy1SbjEfDp/PcLWhs1KtY4l0IuT6RXDmPvbMFxZXT6eUp7DX3teNN1Km/9ZwZilVejTCtBuTa7JqcYRwn5+sHrMt2M0JPDwLb0qO2fAZljkQKM6YjpheWECocaiKiJBpHjmpmgo6sluarGBNJR3gTsc/7CDYQYJCX1NDhBOU+iV4diXGyPclF3qXoFehJ83XdtdThv92hEYWNXkU0vRJ01gyjKGtUKPfui7PbcQdGxw7m5eq4xorqamJHMi/qGXoRsg8CDfoc1jMuTzJgno76ra7kxxYrS4t627Nz7jgjhFjsmGzVUQIZPBVcmYmJpNG9VdHN6T3pGejB4nHbpc25r+mFKWQNQckQ6NmYqexhpDTj/LewZ4ZLSkMfmtV2uc6XGl++QK40tiBCHLYJxhUSJVoknk1+WYqLwqny20MHF0JTem+yR+1MIKxgbJeMxTEDATO9WwmFOaAVw/XM4ea18n32Ne7t4iHOPashjYVz8UFREFDdWKnYcLg6mAPrvP+Kb1ILHyLlwrlyjd5sVlCOO8YjGhv2EfoRRh3SL9pAaltmgcKgRtS/C88xA3uTozPhqBicWfyO/MUg9qE1BVjxeZGbab+hzRHsue7h8bXsSedBvOWw0ZPRbMlF2Rmk5FizfHGgN/f5B8I3lRNRWyGi6iLBSpM6by5R1jcSH24WihTaF3YT/iuiPg5jnnAGoz7SQv3LKAtq254L2DgVhFPghIDBLPrdKDlTWXddnnG2IdJ50NHzhe6R6o3azc2xrEGTtWspTO0W8Oc0v+B0OERIBFvU+5ZjXoMj/uvGwNabJnL6VhY0FiE+FuIUShSaIf4pejmCVyJ2EqKOvRMGdzAnXiufX+JEEuxEmISAuCD2DSH5TFl8JZ9Fw4ncpeJR80Hr2evJ2HHY3bBBnDF7pVM1HrjzLLacg3hSIA2X1P+ZQ1uvJ4r+ksFmotJ7Ik0aOi4v6hOaEVYWJhHmF3or+lg+eMadBtFe/jMqP18rkCPOBBBoSISHKLEc5pkYoVPpdR2hQbnhz/Hc1e7t8sXpeemBzEW7iZr9d1lN6SH093i6LIdUTkAKs9jHn7tmVy0nBq7FCp3ueV5fujPOLDYT4hZuEdIaciH2N/ZQcnYalZ7LPvdHHpNZL5kP0T/8XEN4cGixhOTlHe1FZXZVmS3CIcWh3L3s8eud6f3g+dI1vumY7YMVVA0llPFkw5CQyFL8FpPaA51bck80xwFS0H6nOnoCXdZDnia2FYoSKgqiFZYp+jRGTR5w+pBaui7nwyT3W5eL28RMA8g2hHfEnejh0RrBRflwAZsZrv3M2eZN6fnwbe8N3dHg7bwFnFmNCVCxLG0BTMlslUBOOBsj5iunC3FLOUcLetdipLKASlwyR9Yo1h5WDtIKlgtOH54x9kz2cA6NpsBi5e8UZ1sDg4PI8/3UNphunLBQ460SaULxbjGOVbIZvDniFej97knsye4p44nDEalNguVjfS9o+mzKKJI8Wjwip+RXrpdydzarBNLVqqu+hdZcUkcyLfofLhQiEwoa6h2OMNpKYmnajHq2PutnEitLh4fzsGf7uCyAcfCinNZtEYU4PWzxi4Gq1cP93UXkWfVx8JXg1dThx3mrqYiZaIE6SQtA1CyceG3oK2/qg7sfd69CPxJS2zKpkoO+Z3pEli7CIG4aQghmFjIq5jI6Qn5mGof2rnbYHwtvSa97a7If8/g1GF7soozNDQVlPeFiwYc5ogHLGdkJ7pHldfNB6tnd9ciNpPmKfW/NNqEUpN7MpWRy5Cej8c+0c3erQVMbftU2uu6JvmauSuYuIhk+F6oNphRGIkIsjkcuYmKBhrFa2TsLdzWHeq+vD+VEKxBgrJRAytUHmTGFXQmO2alxxx3V3eFR78nuRedl1j3HEaJFkHlnSTkBENzjwKKwaXg4XAW3tYuF80anEr7xKrVyjm5xwk/uMSon1hAiDT4YMiBeLd5Bvlneh6qpPtcrB/M2T3Nnp3vvjBj4XoiRINHg/L056WAhiOmlcb+N0BXrJe9h6KHqldoRxJG3qY1da8k/wRXk3Kyo0HewRbQBo8tTi6takx9y6na+towue65PtkLiKQYR8hliDFIZCiS2QMZVYoMWpsLZQwBrM1dvL63T5OgWuFdEioDBlPRhL3VUxX99ocHDxdIR453qce496JXaLcY1s3WQ6W0NTw0fXOIot/RtbDw8B7e9x5F3WAMqHvMKvhKjWnoOUK45ziJ6FJYUfhNeE/ot4kRuYRJ6aqCm0TsAAyj/ZRunW9vcF+BTnISUwuz90ShdUGl9GZ6huaXOBe2R6FnsLesR313Wna2pn/V2bUu5I8zkOLR4eQxDxA3T2i+MP1hnJOLqLseiml5xvlK6Mb4lPhcuEN4VIhs6K1o3OltedNqbhsem84cqC2NHmOfODBf4RHSE2LsY340elUsNdAGX8bc9z3nixeSR6SXuzeHR04WxLZcpe8VJGSTE7VjHLHf0QcwLz9brmF9mfyzO/rrNZqMOej5fHjrSIvYZQhIaDWoQIiGuNkZOanjKoLLGWviHLPdZ55or0EwKYEBsgpS4rOOBGiFPrW2Bn0GwodE53tHo9e3p8C3ejdMJv0mVQXaVVEUrfPD8wSiKJE7YGzPff5l7bbMsDwe6yt6iMnSeWTZAEikiFA4P6gyyEfolTjpOSR5yNpRKx5Lm1yYfX1+MB9I0BjRDHHSEstTkORrNRVV3iZQlt/3EQeIF58nuNefp4pXXgbUVpqmHCVcJKYj/CMV0l2hPWA9z5feop21nMScF7tH2oNJ8ylYKPLYvahPCEKoN0heGIVYzOlaecm6PKsPi7OcZd1MPin/ER/yQOIh0jKOM4VUWeUNdcd2SSbLhxlnf2ewp8YXp/eQd3G3BaaBRftVYbSy8/wDJVJdoWOAi/+vnqVtyyzoi/jbR4qTygtJZTkC+KAoh6g6eCyIPSiMuMkZEpm5Gi36+0uCfFLdXo4EPwwP4nDI0cSypSOOhDHVBvW1ljGWxOcbV033s9fMB8annKd1Nv+WnPYCFYRk5+QcozIyW6F1IGPvmj6/bdRtHCwS62BqxCoBSaSpJdjCmF44XChWuE34Usi+uRXpiNoxGtYrdvxfnSqd9K8Of+BAvoGxAsEDQDQfROnFi1Y7Vo7m4Gd014OXyJe552UHXWcM1pkmKxVwFPe0ILNiYnnhjvC/X8QO6L4IrP5cKVuOGsdaMEmjCSBIkGiViFCIXwhUCGhYunk++XnKG2qvu5AsWT0YbfSe5e/DcJBhjiJU41w0CVTCdZG2ELaRFvFneweOB5jHu/eRV0UnBBa5Bh51miUDdChzYCKN0cUg1q/d3vQuFa0RPF/LgjrYiiuZtKkReMAITdhNCEv4XWhsyK/pCMmY2kyKp4tq/Dds8R3hjrAftJB8kX6CbjNP0/EE7sVXJh8Gt7b/p03ndFfDN7dHnoeedymmsbZPhZqE7FRbA2zSprHaYK6f6f7yDi4NTsx+u53K5DpF+aIZAWjZKHuoa7hVaD1IUXi7CQq5lpnyaptbWGwJnNFtwh6oH4XQkzFsUi0jBfPw1MDVZvYPFoInHudKp5d33QewF4QXbTcQFu8GGoWxJSa0TzN6sqpR+7EAQBIvC442LUZMknvIKtbKX/mJaVRIwEieiFPYVqhWeGgYpejv6XQ6CeqPK278B6zT/c1+k++FYJkBa1IdQxXzwMSoJWi18dZjNsL3VJecl9jXq2e/R3/XKpbAxl01uNUShHQjphLMge+w+qAET1YeSS1gbIS759sG+kpZ03lQ2OmIjuhO+FTIZ3hUKLy4/2lpecOafPssq+Dsui107nMPWqBPwRZiKwLbY8Pkm6Vr1cAmiibWh213gKeA97UX3GeBB2nm3GZahcWFVjRZ86ei3WIMwQjQFR9bPlBte1yDG9c7I3pjedxZMAjgSLjYZihTuFNYfEiLqO05XfnainDrOhv2HIztgE5Ub2fwJiE/0fkS/9PMJHvFTZXZVnwnALdXl5S3p0ftV6iXg1c3RuNGhEXKdTPUqHPSkxlSK+E9oFtPVV5/bXSc1ewqqyFqVYnhCWjo3JigqHWINQgk6H94kaj0eVoJ6zpu+x3b03yG7XYOMR9OcAkhNRIW4ugzqqRHJSoFuNZbpuRHOwdZB8aXnqe8V4KXYyag1lpV5AVZxHvjpyMaAjxBNBBX33P+dV2g7NuMK9tjWoJp6SljiUyIrhho6FyYKjh6OIlIvfk/2c86NjsKq8R8l01QXkefIKAjkQqB48LJM54ERlUH5aD2Yba1RzaXc0ekl7HH5SeFZ19W+laQZhZFYnSbM9wDJRJNgV+wdL+IrqjNsx0GnA17ToqnKfxJdlkNaLUofyg9uDe4QlhzuNzJOSm4Sklq5mvP7FGNYg4lnxbQDZCygdPiunOqRE7lB8WqRj8mzfcdR3ZHrSetV7ZXcOeH9wWWpxXBJWW01JPekz7yWMFs0J4vns6j/dbc9JwPSz4atTotKWPJG8jGaGeIMShZeHhYoVjcmT15peo/uupLogxunSiuGS76v4/A2YGvApsDaMQjVPEVqxZTlr23JkdEp5Xnxje554g3b6cOJpimBgWaZMpELwM1Eojhh4CS36Sex934jStcQmt3GsbKPomZ+R24oPh1KD2oPmhgyIM44xkzCZv6J8q/64Hsck0lXf/O0s/e4KbBtnJwE2IkKIT+hWR2KwaihyRXbze0t8FH2GeDp0anGwaJNiv1fvTCVBFDQPKX8ZQQqJ+8LteOCF0ovClLfAqp+iJZkckqqLyIp1hYeDL4Wfh2iLMZIZl+CiBq0Ztx/F/8+Q3UTty/qjCuQYQiUzMvY/x009WZNfnGkgcTx1PXlWfBl8G3vfdl9082rsYklbOFDlQ/k1jCgdHWUNAQEb7n3g8tJzx0q37a0No42YKJIZi2yIIoKxgVOFMIe1ik6QnJqSoaOsO7cmwkLQOd7T6gD72wm6F1olKTICQW5LmVZPXzZoMW/MdPJ4wHqwen56IHj/c+Vs32N+WqJQfkLeOGEqVR1qDhj+nO/Y4dPS3MR3utquiqPqmfeTUIsqic2FPYTIg+OItoorkW+YCaFbqtG0f8BqzkbcKeyV95AHexYZJsIy6j78SudXxV/raIxv4XTGeWZ4QnsPeLF4/nKJbFpmE1t3TmZFZjo+LYEdSg4lAL7xVORX1IPHu7uSsnClJ507k0iOOIqshd6DLYWWhfeIcI6il2+d8agYtJrC1cxA2wvlfviPBKoUYyIeLzw+MEpbVuVejmeJbyV1iHmGe8h4tnwReVF0fm2BZZ5bwlS3R846WS2PHRIPBgMX85LiJdlHyEm9IbCQp8Kcd5XhjnWI8YQNgoqF8oU5iz6P2pWEnzioIbFawF/Lkdhk5iP3KwWHEw8jFy0nO4RKVlP+XrBmc2+udK95IHoqftN643ctdEtt0GZMXptRfkbSOjkvPiEKEcsC6fUJ46zZ6sqovYGxQ6kEndSUQpBjioiGqoVfhf6Gy4ofj6uVVZ8PpxiyUryWydfZnOf49LIBERBPIcIuCjjuSCRUl11kZZRuEnQOecd8dntvfMp4PXO1a6FnvlyXUqhJpz4NMFkh5BMrBp31tuUq2y/LCr8ntKSlM54Nl7OPT4yEhvCDT4M5hq2J2IzflCudtKUhs9W7NsoP1erlAfXQAbcQOh2eLbQ3nEg1UxFcXWYEbZB0pXfbeEl9f3ymdhBzgHAQZ4ZfZFfaSVE9tTHfIRIUqgck+trqUdqoysvBarJ1qp2g6ZbqkEmLhYhzhXOD9YPTiLKOJJQvnDakm61UvOPIF9TI4nDxhP7qDwMdii2WOOtDb1BrXt1jx24uc+l4UnlDe0F97XiDdkRuPGlqYBZXMkmwPVkwMiNAFZ8JZfyM6aXbg88Owfu07KnUoOaXZ5GJif6ECITOgtqEEommjaSSY5xgpEitwrjWxYfTjOEv8Of/qQ/xHCQrgDXhQ5FR3VylZOBrKXSIcyp7znsCe+V3R3Z4cKdo1mMpV81MzkDyM6ElKxZICdP5husM3x3RdcH0tfKraqEamAqStYs4hyiF8YTJhmiHYYzikdOYaKM/rGS7ucRv0rDhIe8+/kQJ4xo4J5k31UMlUGFY+mFXay50sXUgeXp6eH5WdnZ0m3EYao5frFniSSdBfzQ3J90awwjn+RPs99+A0JPDaLftrYihSphnkiyMG4jGh1+C44LchjqMtZAGm2uk4qtfua/CGdCI4D7v4/uVDO0Z+yg+NUdCME38W6NgP2mVcYt2tHvAey98NnkndYpxA2psY5xWAU1/Qj00aymPGAIKSP3n7LPfr9Kaxxy3JazMo92YI5I/iruHRYW9gvGE6oUAi3CQLJlPoM6q8rfGwpjRrN5L6xn7kAhEGW0mEjS/QdVL3VYjYBlp6XBgdoF6fXiBejZ6cHhOcZ9trWJtWQNPwEJeNuIpBBrmDgn/o/Ji44vULsQEuY2u/qFinOGStIyniB6E/IO8hR6GJIyRj8yWsp+JqgC0wcHK0CTd/Oql+8MFQRezI3gx/T9VTNZX6V4oZxhzUnQ3eFJ82Xqjed10aHJba71kZVm9Tt5CNjiiKgYd2w7J/17yN+Nx1jzH+Ln2rhOlLpzGlLCQQYj4hTeFG4U8huKMqY8cli+gLaqetRLB29Bd2tTnyfeYBxoVBSNmM+I9iEoqV3pd5GWybs90InbheFR6DHvMd/pxU3CjZrJbyk+YRKk6FSu/HEESIf9V89fjKNiiyGS8WrIjp6ubCZajkFKJfIYBhNKEn4V5iFeOQJhfn4CokbOTwLTM4dpG6O/2LgV5FRAi8S9VPV9IjVQpX59noG4mdLp49Xofebp6c3a2cvxvT2SkWsRRske6OaQs1R97EsMBnPMr5nXX88iivZyw86eJnGyTxI4DiNuDyITYhE2IP4mEjieYMZv9pPSyXr+HywvYJ+Ww9MsFoROUIV0v5TsySTBUy1+9ZgtvtHUueRd6IXzMevp3LXMDb7tkIl1iVetHUTueLhwg+hJ0A+D04eVa2FfKM726sdOnDp2FlQeREYm6h6aDdoUJhzqKMYz/kx+cZqUdsyW+HsvM1l/lkfI3A5sP9B5cLSA7w0f7Un9fcWe6bf5053T/ea55C3pBeK9zqW9HaA9dCVXeSPU8Sy67IL0RGQXL9wbp19gty6y9ArRSp+SdqZQIjvaKmodshb+GbYRZjPGKF5IfneqjHrBZutDHudau5NnyLgSpDiEf8ioOOmZGBlGcWqhkjmshctd3FHsufDl5IHm8c2RvgmcpYFZV5Um8Pb8wuyOcFhAHl/ip6+raZsw4wXmybapbnkaX7pGCiXSIiYawg/GFO4gwjR2Urppkpoqw2LqiyBHSWeVP74n+kA/jHFkslTgHRWpRT1yyZTJsHHJWdbp5S3vMfCl4snTRbixouF8QV1JMCT6XMyAkbhYzBVr4nOv73HHOIMBWtUyqqqDjmNeSP4oNisuEO4Uihv+GxYzckQ2Z+aOvrZy4HMiI0svi1O00/yYNGx06KQc45UIbT/5aa2PObOtxm3cderF3FnsaeeBzY3Boa+phWldSTUNBzjIZJhkZTQpO+9jvMt9tz0LChrVMqzyho5dNkBeMRYdmhGiEQ4V9hx2KQ5GsmsahhK0huHXF69SH3wDwEfqYDGwXxSjmN8hBvUw8WQxiSmv6chh16XqdfYp6JnpwdBJwSGvCYElZbUy/QVszzCZGGYEKx/tR7Xzek9L0wyq2pqwzpLeXNpO3ipGJ/4VfhJGGJIisjWaTMpl1oSir7bkewurSrd5Q7eD6Gwp0GU8n8DPVP+JPZVimYCpnIHCmdvB6kXh1egZ4I3gLcWtpo2N+XMdQ3UILN00oUhnoDFX+d/EH4dTUx8RzuQ6u+aEam12S9ouZhiGFwYTWhi+ISotvkUGXBKDbq/S1FcHkzVrgtOqz+yoKvRnkJK0ySUG5TOhXr1+Zanpvf3YZeRp8nXxqej55V3Eaa4Vjj1hVUQVDGzehKXMbzw1a/e7uA+FQ1G/IVrr+rzqkc5mpkrqLJIcnhZuDkIQ1iWuKeZF0lXyh8ahjtV/E5s0E3zLqW/gzCJgXFCWRMs5Aw0q0V4Bgl2jnbzJ3cnqIfNt69HhueCtz12yzY/JbElKyRiw3gyr5GhcODwB/79zlodKUx8K8LK7votab1JNNjMSKvIa1glWGYIVnjIWPo5WFoXGoWrVZwtPJ7dmh6D33+ga4FBcldjBvPUNICFNFYCJoTW50dsB4ynwdfIx7W3Vbc+RskmQdXcdQpEZeOq4rnR55D88DdvQ75GLW18cBvLmvE6T8mxGXX42vigyFGIQPhZqGT4rAkM2Xjp5Aqsq0vL05yhjZb+jM9dsFihUAIFAwBzxuSiZUvVzHaIBxoXX+eIZ6sHyoe1p5fXIKb+lmtlkoU/BGtjz4LGYg1g4hBYf0aOTk2A/LLb3/sE+nkZ2kliWOSofRhkeGb4beh6KJGI3LlUWcJqe0sta9tMuW2DnmqvRSBc4Tox75L+M6+kYrUoFeE2bZbfh11XmxeNF6Yn57d51zk23IZw5g6VbsSLg7Zy2pIAUT6QN49YXmi9iVy6+9F7T0qPydoJQwj12IL4YRhv6E3IQZiouQ75JenRinTLLSvbHKmda/5tbzqgNAEb4f2ivoN4xHL1MFXAxkfmpLc1J1LHtLeb56FXhFdbltgGliXflTP0p/PIwuMiNqE8kCWfbX6cbd3Mt6v+20WKmYnnGXPJAxip2Hi4Qugx2FoYkCjpGTRZvjpE+v3rq0ySTUmONm8xAAQBCLGdYq+zjBQz9RpVo4ZfBs63DrdUp6zHzCehl4UXSNcA1pp10cVd5K4D4MMtMk3BVmB3v5EOlP2xLNTsA1thmpv596lj6QP4q1h/WExYN5hA2K8ozzk4mdPKX0rl25GshH1WnkwvDm/noNnBzBKQg4w0Z3UTNcWmRPbbtx9nbxeYJ8GnlleVZ2kG7UZvZgYVjwSo9AETHyJOQVlQgW+h3rFN3fz+vBHbZhrCyeLpeajwaLmIhRh/ODH4gKh+yOu5C3mr2jja+Iu1rFFdJ54VHwMQD1C7Ub9ycIN9tCA1BHWmJjdmq/caB2i3vaewx8GHqUdvdwhGmWYihVFEwTQKQ0OCVBGAAKpvtp6xHdWdJFw0y4iK01ov+a0I/hi4OFfobJgo6FJIaBixmSKpuooYistrhtxa7QSOAP7/z98QrPGvImGDcCQmxO/FdLYq1qmnKLdc16MnhNepV5a3SOb89qu2OVWbdPGUGDNfglYRgCCyH7vu6z3oLPz8N3ua+u26LDl06SeYsNiSSFfYPkg0iHhIw7kp+ZMqKard64jcY2z1veoO0E+5AIvBn8JL4zAUL4TJJW92CXanJx6XSseIJ6m3xSerh2mnB/bDVjH1tdTg1C6TeHKZIbfAzp+0nvPuK60c3GlrfUrjyhIJqlj0WM6okHhtiDSoXnhaGL547HmOCiv6sztbrAQs653IXr4fm1CdwVRyTSNOU+OEpiWIRiyGrLcYZ1g3o5e4h99Xrbdbl19mlYY5hZGk9+RcE2LiqGGmsOAAC17xvkRdTPx/C5+a1ppnibq5N/i5mIPYQPhBSEpohmiZCPr5YjoseqxrWLwHHPKNvt6ir6zATEFpgkxTNOP7FJwVVeXzhnkG+leNF4unyde6966XjXc59sX2WRWm5R30YUORor6B3bC5//5vK+4yLXUMchvOqwYaT0m16U24vnhn6FSYW1htCGSo38jzyWoJ2hpxK0lr8Iz/Xb8uZx+HsHAxYYI6Yyfj2lSGpVJl9RZuxvlXN+eDx7DnpFeCJ60nLGaxpnNluxUcBF5TnLLBsgPA9SA/LyReLm1vLJn7sAsHWlAp8TlZKRt4jdgzSFCYcwibOI+4y2lJ6hpKZjs4O+B8sw2zboL/bsA7USfyAdLzo9g0eBUm9dn2aZbkJzx3iGfbV7BXvkeDhyIW4XZO1fKFNSSJs54C/kIqoVCANf8/nkYdd5zf295LHnqEqc35U+j8mK8IcFhJqD/YTBiQaPUJXTnZin5bBavnXJz9oW6anzLgNJEiEfaS64O/tIxlMnXC1mdW5idL949XqgejN6ZHcMdD9vDWmpX/BUCkkBP8MvOR+sE+kESfVz5svZjs1avluwBKYynKKV7JBoiRCG9YP9hI6GGInwjDGVaJu9pW2wtrx0y4TXxOOr8t4CGhLhHfIrdzsESd1RbFzEZgJu/XOheNl7NXw2evN4L3VEbTpouFxQVsdLtT2YL18kXxR1BA72ueou3LbOKMGRs2upHZ6IlpePNYyFhk+Gj4MLhZSHAJCPk06cM6ZUsS69NsgP1z3jZ/JJ/7gPmh7kKLs5q0eUUpdZu2F0bIhyb3g+er97ZnuleK91a20ba5BfA1YpSklAHDT7JKwVOQn0+u/q2dvRzm2/HrXXqsqgAZnKjkGM24VGheKGdYb3iXWNWpQrmjKniK8WvJ3HK9ST4S7x9v7dDYoa6ylTOKJGrU8AXEZjEGrab/x2UHrVfLl41XcudeNup2qtYERXyUogQfsydycfF5cIGvr56U/c1NDKwKm206onoZqXxpJCjd6J/YTQhjCGWIbxisSRspgwoqCrC7lWxUvS9+E/8b/90AwDGwwo8zVVQ8VOCFk/Yw5rmHTcdcF6tnvOfJd4lXeKb25qEWFcVlpMXkJuNIcn0hQvCrf77u2a31zS88JDtvWrJqNCmimSbYsphqSFiITkhWGHfIxakyeYiKKhrVG52sSK0cvhbO1c/qMLpxj8J7s0hEBqTKFXCWJzbBlyF3WceKB62nuPewh4E3LVagJiLFvKTh1CFzSLKjEaaAkS/HPuWOCE0T3GwLaarmCkl5jgks2JtIdKg5OFR4WohHuMOZD9mbGggqyutVfDj9ET3tHsE/sLB+oYaSbFNK1AaEtkV5hgoWpYcTR1rneCfI97eHjgdYZyKWtCY9FXGE7HQrc2zygkGxwNaf4P71PhI9Ujxim7b6wIpRuZE5J3i4KKNITBhSKGeYaEjFGT15d+odGqW7URwlXRDNt96jj76Qg+FRglrjPmQM5LP1VdXlNnKHDsdeN323kGeZd5rnaEcPlrx2S+WDlPcETjN+kpFB4HDqj/UvHC4ZHV3cbWuTmvt6QxmtCTLY3yiBWEaIQMhI6IYoizk0CadJ8Rqgm2mL4+zszat+oE9tEG+RS1JJ8wQj32SmVXcV/cZoFvhHSKeo97uHpbeFV3x3OLaYNlpFqiUc1GFjmDLJ4dTxB7AMTyZeXI1V/Hobs5r9mki56ClIiPiIdahQqENIWxiIGJGY+Zl+acdKg1tGG+HMyk2sHmgfeGBecUbiJtL/w6Mkx5VHpg4WdcbYpyQnfXemV6bnxPebB0xW2bY+9c8VEXRyA5oSx3HagRbgIX9I/mgNbdxha9ULDXpr+aR5PujWWJj4QwhMWCNYiTiOONupRMoJ2p2bGtwFjLGtpJ5+T3ogRdE5QeuS+DPLdHY1TGW49ohW3BclF48Hj8eyZ6d3jKcc1u6GUpXu1SXUngOU0uFSV4EuMB3PQ05uDXZcmQvpawgacNn5aTdJC7iF2F6oa/gvWEc4p2jxaXCJvtpeWvNL0lxzXWTOZa9awBPBBhH6EvljmPRq1UdFz+ZZ9q23KXeJ56pHyaeyd3BnXkbjhmyV8HVCpKjTxKL00jkxNOBUP2NOqH10PKeb+4sj+oNZ4jl+qNvYmYh+KEiYKnhoqJzY82lvCaR6cfsXm8FMjm1E/jKfIkAQsQmh3lKxs3a0YDUldb3GMWbNVyuXYueAV8iHvhePR1d26DZmxh5VNqS5k94DC+IokU5AaZ+EPqFNlzzFrAELT4qjGgrZi7jgiKR4aPgweCLYWziLKM+5StmeqlDrBHuSrLktOL5STy6AByDHMdICmfN5BDsFPyW0pkGm6ocpN14HhjfNd60Hu/dGlvJmgNX4lYW0t/PYkz5yQfFTAK/vnB6VPcmMwFw1G0AKtKoNCYRJBEirSIE4RghLSE7YkDjxeRVJxcpaqtP7vcyGHUs+Jj7yj9tg3xG/IpdDgDQ1RQ0lwuZIFt7HIKeFB7ln1MexJ5aHTPcPpplWFyWE1MBkLVMZklbhqRCN37xeph3ezPXcOJtyGrLqHXmPyQVopNiK2FtYMyhhCG9YzekRGYi6Jwria5lsQI1CDfxe0j/+IO+xhfKaI1+0AzTFpZe2KFaEZyrXVqeKh8MHlQe/Z0om+vaaxg9liXT6M/OzTyJMsYowoY/vfrx94m0q/E8rf+qs2gl5ynkMSJL4ihhoKEh4c/hsSNjZH0mbajTK03tpvDe8/u3oPtrfxpCsQYWij+Nj5Cek75WOVjN2nGcQR2B3q9e656EHr7c2BxhWlyYX9YB093QiU1/iYNGjELBQAz7vPgTNBvxhK5oqzYokybbpFfje2H9YUwg+6Emokxi9COWJpEoVWqmLXdxNfPNd/m7Ob8OAk7F9MkLzIiP3NLJFa9YpJpT2+vdnx6BHzFexV6Infeck5s8GHeWYNP1UTtN3knXBubDj7+OfH+4cXTSsbhueetbqRamSWTwIynhViHpYYmg4uHFYzKkBOYr6DKqpi0/MO70Sjca+sR+tgHmxY8JP4xQj6WSn1XtGD0aVdv8XS1ebp7E32keH52+XEjbWVjhVs/UY1HHTimK+QcXg/UAHnzXuIq1abHjrvIrXmjvZvElNKOrokqhhmEHYbVhs2Kh49glu+gH62ztX2/xc6x1x3qQfgmCNkToyN8MHE+j0okVJVeYGcgbYx2THlYeh19dnl5eLlxLW2MZGJfrlN2RdQ4VSsJHWIQ5gBS9FPkHNd6x/K6lLFQpomb2ZSijHeJQYWXgx+EOYiAiRyQ6JRxntmoD7TjvYjM39qC6Yf1MAfOFVMjMDLMPCRLjFVWX/tnFW6Ic8h4IHlNfLl6z3gSdGZv6mQNXmhSA0fzOmEuKiBzE3IBifNs51rW58jsviuzGafbncKU7Y/8ituHlIQBhQaH2IrtjhuUVJ6eqNWxuL7Byn3a1ufI9i4Eaw9wIQ0t+zwKSIZUrV5RZTVu/3Qcd9R6g3vGeex4SHWybo5nBF3UU0hIYzwaLXoi7RLcBTH36+ew1y3Jp75nsauoJJyWlzKNmog0hTCF9YT8hR6Gx42LkhGdlKXesHm6OMee1gPk1fT/ArUOOB8zLGA7HUgBUSBdSGVnbmtzBXlSfGV68XtnebJ1ym9paAVeeFTESeM9nDETI4IVBgYW9lDqTtmRzB7AzLM3qd2eJJbpjqyKjod3hCCF3IURiBGPR5ZGm7WmV7AiuwHIntZL5kPz6QH9DXoePyzfOl9HqFEEWk1j4Gurcsh2fnsWe7l8M3jpdBNx2WjVYDxVa0qUOx4wIyRuFGwH6Pvm6ODancz+wZKzlqp8nDqWi5EFiwGH4ITlhIyFlIkTjyKS5JoqpMitzLrTx5HTCOCq72sB9Q4eHYEp+DluQo5On1ssZWdrZ3KddUN5Yn21eQ13mnRkcBZmCmBEVpJMaT1kM8IkCBRLB6D5IevO3S7OQcC7tkOnq54ZmN+R2IlUiTCFHIMDg/uJHouIkC+a+6PgrFm7osZY1Drjtu04/esLKBsCKOA1BUOFUE9bP2P+bPRwGndleDd7OHqVeRB3QnG/aQBhaVZuTOhCSTLvJG8ZGwis+wPrmdy3z6bDdLZEq5GhEJq3kq6KvocXhV6Fe4RBh/CKPI+Oml6i2KzxtxTF5NLU37HsEvsuDWMatyenOI9C3UxGWHRj/WvUcPV1i3uUe8V82HjcdMlwQ2rhYZtYbUw3Qvk2PSmFFx4KZPz168zeDdE4xca5N60uovCZcZIVjhWIu4SehPKG8YhBjf+PMJl6oE2ru7hXxZ7Pmd/57Y38UwmBGcMlkzRKQPFNPVhoYc5q63A0dkd4YHv1enl5I3YAcvVseGFFWjpNgkIANt4olRsFDc/+Z/AF4wzTzMX+uXeqFKTXm7yP44tOhqmFLIVygheGRYxHkpmX959mq3q1TsNp0DvfD+yS9kgITRi8I180gUAGTWpYRGNlaINtK3dYejR9gHtneox2nnIdbLhjUlqdT9BCqTmrKrscEg/T/prx1uHZ0uzEWbrxroOk/Zuekn2OlYj8hSaFSIQ+iJSLiY9EmCueeqovs9PApc632x3qQfeSB9wWXCSIM8c+P01LVulddWdBcMN0TnnofH57f3hRdfBzWGxXZcZZWU0PRBI4aywsHsEOYABY8mHi8NL+ybO5EK/Uo8yaOpSxjBeKUIVphfOE5Id/iqWSc5Zbn8Go8rUtwGLMNtts6cH2jwUgEX0iPTKnPIVJkVSDXrJmsm7vdjB3lnoyez59enl1c+Jt7WN3XTVTW0iBOzssIh67D24DF/EW43rWTsfmvJuwzKTenI6VNI7kiTmFBYUthkSFEIv9jj+WYaE8p4i0Mr5hynrYd+fO9rcEFRXBITcv6jpwSBhUiFsZZepw9XPRdzB7w3oGfPJ6i3PNbBBmUFyhUl1HxjzcLl4fOxBmBev0rOeS2QnH+r2AsKSn+ZzsmD6PBoh1hl6EMYNshh+MepDVlRie9KbqtBm+E8n219/oNfXVAkkSyR6FLXk9j0mxUQpd8Wa/bYFz73e/e9t8tXqueE90n26cZmleZFQsSPY7xC9uIUsSRgX69fLpG9kPynC8TbNzps2eVpYaj7mH+4VjhZSD3IW4iW+OppJsnfymZbAZvPfKd9YT5iTz+QLCD/of/y2sOUBFAFQcW4RlGW1HdZp3I3uUel574nxDdWNxjGeAX3VXdUlHP64wyyEaE6IFafb86RbaOc4UwIWygafPnTGYOpHTizCHsYGehXSGoojdj/qRnp3npYqszrzExq3UEuJ08zkCwhAlHe0qbzkgRTBSuFkfZV9twXMweMB7t3gGe4B4D3TIbg5qvGBGVppLBz0/MXEi7hXmBMn5BuvK2+vMA7+5tEqoGp5Ll/aQ1YnDiFKF+oWRheWIYYx0lHWYb6S7rq+7F8Z707PhwvLFAAMNhhy8Kx450kVjThdZrWSLbG9x0nbveLR7dXkTeqh1QXL8aYNgIVYvTJA/BzQkJNIU6wjX+uPrPd3Yz1zDnrecrU+hKpX7kR6NgodPhYWDVYSQiJaKLJJ2mTelQq5quZPFL9LF4lzunP2iC5cbQyiEOOBCBk+uW15kw2ngcjh27Xk8fE18dHnbdfxxm2mRYuxVu0wXQbk0ZidJF0AJJvyp7NHeU9Gnw8S4tav7oj+YtJHAi7KHRIMNhJWHcIe6i6uRaZoupNytqLn4wyjQGt8569P6+wlaF94nSzUoQgNOJ1c8YX9pSnE7dWV9jH4rfMh5aHVRcnhr5WARWj1O2ESzNDooyhaZCy78MezB3+XRW8X4uNatRqSBmMSQi4odhpWGp4RWhQKJ84ynkvKYR6T/q/W4hsPO0Zncb+t4+QIJ4hjVJnYyZEBaTXlZXmCMaalwPHMhec98LHuKesB3v3LWbAVjZFpGTy5ADDWZKKMblwyz/hfu3eIR1L7FarnUrdOkHp3Hkw+M1ogCh6uFPYg8iKmK4pHnmIShuKnHtyvEh89+3Lvs1PYFCRAYhSWHMqI/j0zWVjhfcWgFb6B1jHiseu55FHn0dapuW2w9ZNJaglK9RM41TitdHIwNH/8w8Rrkp9WSxmu63q7GpFOaFJU8jLeFa4gnhPGFloY5io2TYpjsnyqo0bVdwTDLANsE6nj3tAh6FTsl8jHSPpdLmFR6YP9mxXDHc+l44HhgfHd7UnY2dHNtIWPPWvtQPEQIOaspqhvsDikBlPFU53fV88c2uyCvBKXlmDiUz4zmiaGE4YFQhLyFDIvRkLeWGp9tqFm0q7/2zB7ZJui+9f4FjxSII98uMz5JS09WC2CMaLNvIXaneQV8WH6CeaB6Z3PfbdZk9Vz0UV5HCTj+LRYd9A9+Aqry/ON911nJjb2dsMamYp3Qk2CNJIrYhEOEx4QigxSMrI4PlcGcV6prsx7BLsxO2fTnkfdMBFITVx+PLs88D0gkVONf12SHb511xni+emh8CHw7d6ty2GxPZLte+1WRRhI8zSwgIBYSZQPs83HmBtfHyxm/lbLRqJicc5WajGeJyoY+hfaFsITsikmNg5RYnLuowLB6vJHLe9ZW5Q70YgTvDyQekC3aOv9HIVMiXQllTW4gdCF5XHv9ezh8VXlVcsdt52gqXTlTvErCO+kwbCIVFLED4PaF5UTatcsCwYO0F6lyoLSWs48hiD+FU4WegjCFtokAkNSVH5uIpVqxI71jx2fWpuW484MAEhFdH4cs5DcrR85RiF5eZNluOnMTeG17IHyse8d4OHXCceZneF8PVSZKiD6lMYkgGxY4A8v4c+aJ2xjMt79Vs/urOKCNlOOSlIcBhYCERoSrhbCIMo1glOGdQqSVr5+7bMdu2Eziv/Ay//kODxxUKms67kMSUSNYcGWja3NyunoQfAF9f3zJePN0R3CeZ0xg5VSkSxw+WjLiJi0VVwcS+qfqNNpxzcLB37WzqsOe95XzkNyLGIdmg+SBFIYNiJyKg5Sbm+Klgq1wtyzHmNHb3inwRf7hDeIchyrTN+hDPlDrWjVlG2u3co108XnWfYh64XgcdVpwPGz0YMVWJ078QG8y6iVDGAcLxPjJ7AXgZ9CZwzy146pjn3uZTZGCil+HUIW/gm+DyIiZjSWSpZqHoVuvi7ruxIzRnd8N73z+7gueG7YpQTWRQhdOk1eCYtFq1HE2dYV5Pn1pewF4enRHclZnc2GfV6tKXEBvNvwnGRgQC4n9Euvm3kDRJ8XIt0usOqI1mlSQRoo1iUKF5IPGhFiJZ4svkfmZHZ9zrRy2qcPu0ZfdGO74+h0LVRtGJkk1vkI3T/9XnGKHaYpxcXZIeGJ8CXxAexp4r3Fea5phI1txUKZEEDYUKZMcjgxJ/urunuEy00TFJ7lKrN2hw5jNkUGMEYlrgxaDNoVFiMOKKZO6laqg/Koxt5DELc+X3hDss/m0B7AZLSelMjlBA04oWK5fkGkZciN1wXeLfb16ZHkVdoVyLmzRYzNbB04JQ6c13ijTG4oNWv/A8GLh09Jixlq6AKstojSdYJQ3jX6H/4TghGiDHYVsiTGPe5jJoEOr7LnKwlDN6NmS65P5AAlbFq8kUjPTQCtNWFWMYPJoEm/idjB64nscfFd553Rxca1r4mQuXItR8EWvN3krpxxsEFH+E/CJ49zUCsf4u1Kw9KXzm0WSII4RiDSE/YKDhNaHEoq4jzaYoaD0qRq1tcEDzeHcvOq8+AQGwxVcIQ8x6Dv2S9VV9l4JaBVubXXJeQF8gXtGeEl3MXTcbNhl5lv4U5NFZjj9KiYd3BAK/0n1c+Oa1z7II70Fr9ak0Jn3lT2NhokWhRGDn4QWh7OJm45OmDSfE6ifsnu/Ys0b2nbmOfVkBywV0iKWMck8cks+Vctep2eHb0dwsnZFfLh8inwTefJz8GsdZnpcHFDmRSc8ni91HhQS5QUC8/3mQ9m/yee9g68oqYycMpW0jkyKwYhkgZ6EiIbpihONBJVanrqnVrPsvi7MidkD6LL02wOSEx0hdy5zO3RHA1PbXJhpk29Sc/R14XvUfHR9VXhqc/BqDmhDW19TfUd6PaAurCEvFP4DufXT45rZ7syDv+mwJahcnROUXo8kiqCGd4FEhFOGt4kKj8iWk5r8pw+x6b3YyuvW6+UT8zsEPQ/YHN4u4TuHSDNSI16rZb9ttnLEePZ6X3qoe413WHT8bQlnH15PU+ZHJD/ZLZwgyxJpBUT0FufC2ZvNfb+As86qOKH8mUqRjYlCiNeGJoF3hkuJWo61kzmchKbLrzO6r8c814XiIvS3AcoQEh7rLA4670ZzU8Vb52OnayxyPnepe+9843p2d+90I292aExfFlUxSlY/GTF6Iq0U/gc7+Dvs/NwpzpO/xLPFqfmeeJeMjbWKL4gihcuFkIZ3h2qNq5PNnFulHbCGuKLH/9bP4UfwBAFuDQAeDSvpOEhEgFKFXEdkQ2zpcm17unnxey16fHd4dqdv72l0X2BW1Eu3PYgzBSbfGfQJBPs66rHbxc2pw4u0m6qtob2W9pBoi+GGKYWjhiGHrocjjcKUK5r9oguvbLorx+rT3OGl8MT/7g5gGr4omzcfQpNN4VqlYqNsUHL2c7x5LnwJfZt67XQTb0Bp5GEKV9ZMLUKLMgUnuxb7CUj6P+qh3p7S8MQMtaipHaDDmgiR8Iseh0CDPoNYhLiFi4yDksua+KJkrKa4ucQm0pjeiu8l/MEJWBvTJwg2G0O1TMNXGmLOagF0+XcZeM57znvLefZ1fXG6aNZiKljYTW1DyDTJJ9YWpAiU/e/tu9980cTDaLncrbWh9Jfmks+KPoY6hNqDXIcniA6L1I+QmMCiWK0kuIjD684O3Ynudvy8CCkcYichM4xAvE2iV0xhvmm1clF1d3qFew59bHuOdpRywmupYrVaVE9dQT42jimCGxAMzP248XPgh9IVxju5J6+Ao6uaTpQEjvaHg4VqhMqGUIVuivuQmpg9o+mq37Qhw6nR/tsR7LT7LQggF6IlYzLuQP1K8FX8YLho0W/adDF5V32+fPx4bXZXdPtrIWQmW/tOj0VYOb0pUhsID4D/NvCu4oXVw8QOuh6uqqImm2OTA4zJhzmHJYPTgnGHzYtskYOXm6HuqdW00791zsvdtuq2+RYIkRYvI4owHD+4SktWPmH9avlwpXUZe5t5rXxreeV1DXCYbFBmOFuvUUpGQTjjKbcdqA1m/8LxE+Un1eDIzbtCrwalppvukROMdIjAgymFT4UDhF2IjJAplaKgBqmIs2i/ac0q2rXq4fd0BjcUKx9lMso/8UcGVSRgmWaBbXd0s3mYfCd80ni0dgZ0NW1fZHtbeFHeR4A67yvfHuwOEQNo8pnld9fQy+O8erA5pm+da5X8jb2J2Ya4greFkYSuh4mQWJfhnbCoeLLLvojM4NrZ57z2hATDEmYh3C0+PAFKU1O4XJxmPG0KdEB5SnyWevV50XmFc8xt2GK5W1FS3EXGPNos3B7IEaABuPY55m7W4smfwZazdaTynvqU+Iz6iCOHHIZwg0KHJYyyjvOU1p0FptWwf7wnzOTXw+c19cIEUBFhHxAvTTzqRr5S2l5cZjJtLnPtdYZ5inwaeWR4p3UAbh5o1FqgVZ1KqDukLs8hwBHYAon1PueH2NPKbL2hsumml56zlieMSop7hZiELoRVhjGLNY6/le2dcaV7r969gsmQ1hzkEPSRAMoQaR/RLHI4OEhXUthc/GNgbJ9zpXhvedd8RHsTdiR1PHBtaI9cVlL2S6g/qC+zIVUSmwe09uvn+9dgy6PBp7IhqAugmJXAj7CJv4c9hRyD6YSEiZaMHZS8m5uln7EvvJXIn9To4nrxpQBYDrAcIyyeOEJFilEnWwljJm1kcSF3Cnp4fEF5rnq+c59v6WjFXRBWoElGP8AyPiNKFqgFA/hM7ULZDdC0v+izkKgyocOVbI9SjHeHYIQcgyyIQoqgjgOS8plgpZWuErsmx5DT2uL476QAyRA1HoUq7DZGQ25Po1oQY39rMXN1dUh65H14fDV4U3bNbvJpZGFPWBdK8T88MPMjIRd6Bqz5MuzF3cTNPsJbtZirUp/UltmRx4lAiACFO4S4griHSIq5kuua3KM0r/i6ycVX1JPhU+2T/TkNMxzFKKo370PUTjpaIWONbHVwcHeCe2p7DHqBeG12zXEwa7hglFiySyVBiDQ6JaYXtwiE/OrrcNwt0UzCdridqQ2ippnsk6+NkYT/hfGFP4Vfh/iMH5KrmNuiE6xkuKvE/NCy32HupfvtDDwZESfiNZNAFk7uV+xkdGnXcLZ0M3lEfLV8MHmpdmRw5WnIYAxcM069QO81+yS7GfALjPyl7XjgutImwzS5VqxZoPCYBZN+jC+I1YSEhTqG3oWDimqR55oioXysirXywSPSVN357Jb6pAqNGX8lrTSIQilNR1m6XnJp023cdtx6cnlOe2x6oXXOckhr2WadW95OVEKGNxQoGBwLCyD9aO7a4lPScMhIugSt1KJDmRmS14o3iOqGPoPwg+WFn4mXj5uZip5sq+C1sMOmzp7ciO0l+IIJRBZzJGQz0UK2S4xWNWB/ZgxtP3K3eWN7YnvSe1Z243JRaX5lY1x2URtHzTk5KiobKQ/6/vXwzuGa1AzHn7mArkKkMpr9koOO+Il8hI6EUYQ4inSIX5GFmFKfqasVsxy/Q88s2wjp2/maBZkUkSMdM4Y+rkkeVrZg6WgHby91WnYefLl8aHmpeGlyc25yZhFeO1KZRW46RCy2H50Nk/808+TmwdXgx5y7D7GjoiCdMJS0jMmF3IKehJuGAYVziqiRVZhlnvip5bRav37M5tkh6fP1mQYxE9gjgi63PABK4FSHX2Zoc2/gdIJ2znydfTd6unZ2c2tuG2ZjW+JS4EdyOjssHx+6ERQBFfGD5fLT5sjbu5WxIKhQnp+TnI+4iduFdoQthJGFx4l1j22W7JxHqcuxR74TyZvYJOYq9lEEGxObIicvgzxTSD9WM16qaYxrkHWTd1V5cn57eit3yHOubgRnCV0+UvRK+D1mL1odcBI7AUP22OZz2OzKVb7IsDKo+JwLlo+OZYoriLqFWISahCuId5BOlXOggKZBsS+6tssY2OrjafIuBPEOsh4+Log6TUdiUv9cJWbxbaNztXWveup7bHyWePd0LW/jZuZfUFXGSDc/JzJ6JP8SkQU79e/nQ9pRzDW+5rRgp6udc5apjcOL7Ya3hAKEaYYJioKNKJEInpmlHrHTvrLHwdZ25dz03AB6EdYcJis+OmpHlVGCXENkgG9xc453t3pUftt3z3iddJxws2jUXlpVmErROzIvESQ+F/8FvPVq6TjXms1lv1e1n6nRn5uXVI7tismG4YQFhFaGeYk8jKmTk57TpMStJ7ptx23UAeNe8jACpA60Ho4rJDi4RfBSJlsZZbBrH3NyeIN5cnzqer18O3Y/cOVpVWELU0hMQD+DMiMlZxh2B735Jusz2z3Qk7+LtEeqeaD6llKQTYu5hVaGFISNhzGJw471knGZZqQ2rle4icar05DjNPG3AI4N3BuLKAI2RELsTxxcdWJ4a190W3YnedB8N3p5eKR0I3KKahJhf1cmTT8/ejH9JckWkwf2+vns491k0GjDG7edquqgN5gOj8aLsYX2g4+CMoVOiBWNEJSomtKi1avjuNfG4NFw4NHtoP8wDaIZtyiKNiNDl05WWJdiW2s0c9V3JXphfLp71HhkdnNykmlMZRBYJU1pQOw0+yVPF/kHJvnH7Yjcis5VwsO3MqwjogmZpI+tiSyHKIU2gwqD/YUri6yR/plJoyyuS7Zmw3HRcuJp7lj8zgwhGe8oHDTDQeFM0VrPYetoiHHldVh5CnsZe+56CnejcvVsUGQ2WENPQUFSNRAo9RmoC5/8OO2S4QvV6cTguP2ryqS5mQGTkoyKiMCF1IN3giuHAIwrkCWa+KIfqum1vsSY0Fzev+qj+/YIixmSJGQ1w0BcTXBYt2DwaMZw13evdv96qHshe+F4q29ObqdkYFloTmtDUTdHKRIcLw4p/RbvOuN0063Fp7aGrlqlR5oxkUSO7IhuhJqD+IQDhw+Jto8JmQKgGqqLtpHBf8863hfs8vrIBZ8VOiN6M14/AUy5VG1fEWn5b95zIXuYe216SnnfeBZzgG3sZGJcKlETR0k3iSoQG2oNtwDr8aLfudTYxy+5masJpKadN5WUi+qHYoa7hJKFrYbNiriRqpZaoI6q9bUGwN3NZtvF6Oz1CgZ2EywlGzEpPW9JUlXsXtVpanDZdHd3iHoSe0J4MnegdONrTGY7XD5SNUeiODEthhzDDJ0Ca/Ms5SDXFci1vCOwqaYVm2+UrY5aiNWDhoYuhQ6JoYkPk42W859dqc2yOMClyzraoekK+LUFeRWAISMuij5STFVT319GaIZsLXXMeCh3DHwaeld4znXtbQBnnF1AUBVIijtxL8MflhEJA2L0oeVB2dTME73Kr5Sl25y5lIGNCImfhdSGXIbXhl2J/o7LlGudYqc1sPe8d8sw2MPknPPEBDUT7yCoK+M5skg4U/Rf1GbtbcVyx3iNeMB7TnqCeQZyxGzoZsxdzVRDSK05Hi79IGsUigSy9F/oTdihzAvAPbDxpuCcW5dZj8iJ8IbkhbKC3oR+iYePtJZLnROrr6+8vlTKDtey5ZHzXgKrEPwhESx8O71I21JDXHJmPG6bdFF3PXq3eZF8UXjMda5ufme1XvRUSElAOqIwdiPjFE4FKfdr5lPZEs3cwCWy/6eNn9iU3I93iSyHJ4Xvg4OEbIvajpuUMZ1wpVmxk7sNxmvUNuSy8H3/yBG7HokraDnWRJNTqFsFY8lq/HOreU15U31UfCB8PXTwb1JmDV/HUd9KoT7MMvchCxXOB7P3D+kV2hfOcMFstcOqkKDtl2CSU4uTh2uFA4SchE2HrozxknqbFaT5rkS8vcYQ1bzjm/H1AL4NSx7pKvM6OkMJTuZbVGRTayhzU3ZiegJ7AHsFdcR2C3HTaNxd2VatSE0+ujKCJPoWqAjc+gjr2959znjBV7WdqsKk9peHj22L7IcQg3eESYgQidiK/ZTNmu6iiq89upfIxNPD40zvm/4DDY4asynlNUBFc0/CWjVjh2rec392lHwsfOJ7DXtzdo1yOmsDYHRXkk1PQbY0/CNNFy4IQ/uL6/DcZM9KxES3RKqroFCXgpD7ifWEeIYWhbiDzIcai/CRdJo4pP+q/reIxDzQFN8S7xT/Qw0iHEsrcjZzQqJPuln2Ys1s627Zdid6PXtge+54l3dkcFVp3mFtWqpKckElNFclshqeC5P7Neye4O/QxsFEuH6pVKO2mrOR4oyqhzKF6YI4hbWHIIoplEmbe6LHrKG47MOZ0gTdRu18+78Lgxg+KD01KkHNTEJYAWJKakJvZnXqeaB6aHp6eXR3enA+acNilVllTzdDNzThKPsaMwwd/UvwMd1D1HvFnbder8ygZZvFktCLGoh1hpuFSYR0h6SLzY9Ll5OiXKrptgrC680W3ubsKPrRCWgV7CWKM6pB6Ey3V9dismjGbsN4MHoXeVJ7MnrWd3tzR23mY45ar09ERa02vyhaHYUN1QBq71Li09PsxY27NbBZorOcH5NXjGiLjoX2hPiIXodMiwKQnpf/n3mozrQXv1rO99q26yb5hwXyFx4kYDAyQI5K0lZpX1xncm/adGd2tHrtfUh7QHm1csVsd2NiWgxRjES0OMwtph/qDjQBAfCB4wrXkMcTu7SuiaVjm+WSH47MihWGmIU5g/mGeooCkV+XhKCRpza1IsDezHHZ6+pK+FIEcxWDI08wuz2ZSr1UjWDSaZRtL3M4eUN7GX3leyh6ZnSea1xlH10MUhpFqzi3LfAfqA78ALX0/+NP1dnIv7rQrnOm250alY2MC4fyhvSFB4cHhViKtIxilDyfl6dgtAa9lM5Q2qzmQvcaB7UVHyGWLkQ8IElbUmNeq2eSbSh1OHcge9t9MnuSd61ybWwwZb1dk1JNSG48FS+vHj0TfQF39oPlhdcjzL2+d7CJpm6bQJUsjuCI1YaQhPmFOojfiPqNCZQ9n5ql0rHJva7LAdf+5Oj0dAbNEoMhji30PKRGmFJqYfFkv2wEc1l44Xole7l5yXeoc01vumezXQ1T5EgqPOkurCAYE3cER/SJ5tfYecwOvyO0jaY7n1GWro97iraGG4XThD+GLopejv+Uq52KpsOxYb3myF3XmuMF80cCOhDfHp0ryjumR6RUSVy6Z4tsjnJfeER5YnyRfLN3gXQ9b3ZmsV78VSlL7z7+MDYhCRRBBTL24ueM2lHKk78htD+oQ6H1lU+OQotOhmSEOIWgh2CGcY9klUCaF6Wartm6zcjV1u/j+vCX/zwRLR5BKiw7b0WSUedbcGQ2awVx9nePeut6+XwpeKB1026/ZkNiUla0SRU/ujIwIxcWJgWV9oDo89umzPvAlrTfqfGgV5ejkDyK4IY4hEKDi4PQif6LLJMgm4Wil6yMuBbHjNXO44nybP5NDhYebSu4N5dD9kwFWv5kOWtHc5t1jngJfMZ4CXmWdABw5mkvY0tWbkp0PyAyhyaFFw4Hz/pJ6prc0s8YxU63Cal1odWYW5ABi3eHkoQNg0uFLogajRKTeZkEpTqvS7rTxMLTguHH71z/9wsCG4knnDRFRGdPPFmBYjlqx3IPdnh8j3gvfEZ4/HfbbzppV2LUWrRLzUF7M88n4RXsCFf76eu33VfQyMF4tcqpIaOYmCqSDI22hkaFG4XxhBKIyIuLkhea66A9q7246sP/z/neLe6m/CsLIRyNJ9s0CkBHTg5XP2JZavdxu3VCeL96Inw3evF2Nm8Ma8thqlmITFVBiTW4KGEbGQtJ+6HsJ+AG1PfE7rXRq/GiBZrfkSaNm4dDg1qCmITrhrSMPpEEmVShK6vnt8nCP9Fq3xDvbfqiC88XbCd3NvRBNUyIWOVjSGyvcoN0AXt0fm57WHr5dHFukmo/Y1FZdk6JQpw3dCiOGlQMzv1B7+/hx9LBxFa5aK4XoiuZGZIBjc2HBYXQgyWFVIS9i5+PJpa4oM6q07ZvwqXQUN1/7dn69AndFOgjLDQQPutKqlZMYRloWG5sdtN3ynyifFZ663Wsc0BqrWM1WtRRY0LZNyUqkh5LDO7/bPIV41vTrsf3uRStsqVfmlqSXoxUitCFcIPqg1WHmov0jpiWAqB3qim2LcBpy8TbauhS+c4GjBU+I78wPz4KTFFXXV+zaOVvwXQxeBB5YXyDfdB68XHnalhkUVuOT/lE2zndKYgePxC2/+bzEOMk1CPJDLuir22mapqJkvaOBImfhQSEfYS4hSmNQJCQlyagDqlps1TAuMwQ2wjqw/gZBokS2CNQLxM8LUt8Vg9gamhDcaJ0bXn/eRt6HHyFeNRzw22rZYtdVVLcRWw60i1oHnUQlQI99IrkwtVrx6O9+q7OpU2cK5ZejyeJuYZohUWDDoflio+Pt5RknwenDrJ/v6XLU9qA6Jz0BgaaFcAhjDDaO9pJpFILXedn8nBWdRN35nvgfMR57XZMc4JtpGR4W8dTM0iROwowKCG6EC0GJvXj5qPZj8ywvWGygaVfmluYfI7oiCaFNoMUhEqJV4mEkNaUVZ7dp7Sy+rtnzIHafeeu80IDpxLDH9It5TuvSJdTMl7IZRhsB3Pzd/93L3wHe+12pXMmb7xmalw3VRhHVzy5Lici3hFvAxH2kOf92uPLtb6+s9WnPp4+lZ+On4pqhx2EnoQ/hoqJ7I9SlGGc4aldsby+jMgw1+Hj+PKlASQQCR9kK0E5ykWdU3FeJmPIbDNzTXgZe0R6+HnBeqZ0f28raDFgH1ZwSPE72C8bJEgTnAXP94XoS9o2zfO/oLOEqHGfO5hYkHiJeIjUhDODBIimiNqO9ZVsmiylrbFWvBnJl9XB43zx2f4iD+MdEiuPN4pFXFHgWsViRm2wdBV41HjafPN4t3yedXxrRmhxYH1YAk2/Pmwx2iK+E1MGOvrp6b/bPc88wkyzxqojn9eW7Y4GiT2HaITFgjiFcIiYi0GSJJyYoy2uI7yax8DUneM570P/hQwhG/IpHDYURDxRo1xtY3tseXOoeCB4FHv7ejh6G3W6bxpqqmDrWD1L+D+5MbEkXhZ1Bzz5JOwK3mnQ9sQjuKOstqEjmt6Pg43iiDyBvIOqhVyHc42Kk4KbBqJXr5i4x8Uh0SLdKfAA/VsNHRqXKu82+kCJTvtZZGPGajhy2ndGeSp8lXyrepR2q3CGamhiyVUKTPJBXjTxKOEW+Qoe+0Pvbt0g0rLEwbhwrXuizpifkDONBIlehXGEVIXthVWLI5QRmd+hUau+tTzEUNL94A/tPPwNDPQZmiZYNlFBPE43V1dhImrTcft3p3n1fDx7iXkYdtpwmW3HYtdYUk8BRL427CcMGXAKJvzF7PvgZNF0xpC7davkoveYnJOljDmIq4b4g8uFYIfmilOSaJgZo6Wq6bVWwc7Ofdws7HT7TwotGDckKjPAQJ5Nj1j/YR9qvG8qdlV4xHuwfOp4q3Q8c6JprWTMV/9O9ELTNkgqjxsIDVf7+u404sLR+8Q3uhuuG6Rjmv+RaY0SitmHzYQbhqWHcIt+kiCZzqJsqvy08r5Ozczbquub+B0HAhU/JYAx7D+8S5pXOWE4bGJvZ3bTeNd8jXwseMV0Z3IXa3ZkPVvcTghF3TWNK3gdqA06/s7vvOKJ1l7I87m6r4elkprektmM44eHg+6F+YcJibmLu44emD+h/KwftabBqM3Z2kDphPVxB4UW3yMWMPM/Kk62VzhfhWjRbgp1tnhzek18Gnq4eKFy92y7ZupaFVFrRjA5OSwlHlcQFQNB9NfjwdVmyFC8DrGxplebOZX7i+iINYQng0yFIYVKi0CO+pa/nfOnEbOdwv/Mytt65wb4CQbTEkci4y40PrlKzlQ3YYVlO29vd0B1qnvieGJ6gne0dQttXmR4W21T40YgOe8s6B9NEh7/L/HC5JbWlst4vpCx2KWZnICUvoyqiQWGWIXTg3+FjYklkLKTN58wqHKxH75fy2rX1uW29fYD6BOHIVUvHz2QR3lTvV9QZ+prh3S3d0h59Xmvel54CnQQbhtpxV+JUE5IaTqYLkEhaxPkA9z1cebD2D7Kpr0ust6mQJ9ylvaO/IjVhVCFqYMfhqSIfpA3lSKfYKe/sOq+isp82JXlbPOkAS0Rmx+uLXQ6uERmUctawmW9brt1e3aSevt56HvSd1F2B2/jaG9fPlWRSf8+AzDkIp0UYQRl9VnoUNs7zRy7ILSBqFCf8JdWjsCKNYi7gsqDc4M/ifCOp5NvmjCn1q6XvaTKzdbT5Tf0uABKELIdsy32OFVHElKGWkhl6G7VcZ157nnDek9763eoc6Nw82XjXjtX4kmoPt4x/yK1FIIGpPjX6IPdPs3Yv022wapeoImW8ZKzjDaIV4YfhEWDmodDj9OSWpy4pO+v3ryexUPWoeXn8Cf/Fw6eHLcq9jdBRYpQZVrxY4BuUXRrdtp6snu2e2R6J3a0biVmNWF2VBpNQkD3MxIl8xQvB+L5gesd2uvNh7/ls1Wqn5+wmfCRNI1Mh8SEhoXmhDOHOI0yk2ucDaRyr0m4J8V+1mLgn+0P/ucMXBs9KdA11kQ6T59ZpmLba8hwJXdmd3x6N3uqeld1Qm8PZwxh1Vl4TCY/KzWPJnsYBwsB+9jr4d4r0E7E+LbvqSuhUJu3kF6JXYfRhTSGmYWJiAyNGJRqmxeiXK5suU3FEtMl31Xu6v3PC5Ua1yfzMl1AEVAGV19jHW39cQR2PHlve6d7+HhZeLFvuGkdYvtWUk4DQIk2kSbeGe8IYPyS7CDe6tGIxEC2xawPpRKa5ZJXiwGHBoO+hSaF+IhwiwqS45g5pOmsRraDxDrSEuGT8Bz8rQmlGDoo3DWgQXpOAVn8Y/tp1G+adGp7AH2Je5F4+nWDcYVpOGOsV59OnES3NtMn0hlZDOH90/C44WPUcsVpuCmqh6U5mVSUD4vihwSEcIOrhl+HbI4fkE6bpJ+KqVe4scI80Cnd+u2g+xgKYhgvJKEzgz9UTVRYV2G1aJlxMXY8eSd7knzbeEp2+HP1akxhz1gwT9tFXTYBKnMbkgyN/ljyLeHW05/Hlbmjr/KjvpthkmaNUoi+hR6FKoZ9h0mJQJEOmC+fDqxStGW+k87u2+rpIviyB38YtiTcM8ZBMEtbVelgZmlJb7RzZ3k3fdl7sXkveG90xm4bZEpaq1FJROc3FiqiHfUOs/6M85bjF9ZpydS8cq1Rp0maIpQzjdWGh4UShcaEJYjliJmQnJeOntSqbrMQwfHNOtov6Lj5UAcKF5kh1i/cO7xIzVUaXl1oIHEUc7553nrnfAN723bFdQRuEWYaXVZTFUf6OaYt8Bx5DSAC8/IV5DrX+Mjau6iwHabdnRyVA4yniTuFKIWXhRCHIIjHkSaVpp7HqaSz57+/zMnaO+ZK9pQEWhQsIyUwnT3KR4VTgF7GZ8VtOnOXd0l50nz3d0J3OHQ2bhZmDF1uUW1ItTmiLT4hGxIdBMz0buXh1zfL1LzMsEepAJ2UlGeN3YhZiLSEMoNhhV2KvI8LlTGdxqc6s6K/pslO1tXlRvMYBbMTJB8HLhk9SkkiUUlff2cEbvp0IXhGeUp7RnzidlB0wGz2ZjReV1V2SFc8BS6XILYS0ASn9rXmxtkUys69nLOtqAWdUJcXjp6L3obBgmWFiIVQiY6Od5TXnmWnja8ZvPTH3NX345Xz5QKaEhQgaC2nO9RFKVNBXWRjQ2rOcQp6I3tre353Hnpwc5xvJmngX+NTRkobP0Iv/yGYEWoGlfh56JLbbc00wUmz86jXoLGVBZBmiTKGtIQVhOiFs4eKjUyUZZwHptaweLqfx/bVnuH28j4Agg6zHrUsujkQRRdR2lylZWBtSHKFd296XXrwel94VXVnb/ln9V35VmZLizyWMnIijhPFB6P42egy3IDNG8HXtNipfZ7QlqmOz4oAhoCC8ITxhO+IHo2XlUeb3aUDsSW5nckb1i/iiPBi/XsPaRwNKV04eEPtTvpb12R/bOtx53RHerR893lOecB2CHBUaq9hdVZjTL5A1DJ+JjoZUAf9+WLr9Nu7zTXCOrWsrt+gmJg0kLKM3oeMhR6FUoj5hNmMd5HwmoykR6xEu2TKudKW4xjxhv4tDj8ZQimxN5VC7U41XaNhZmulcvZzv3iSfNx6cnkEd6RvH2l4Yuda40zEQCg1mCcpGPEHr/qn7eLeStAoxK+2MqvtoKaZe5C9iwWE1oSVg0aFvYkmjH+Rs5npo7+rFLo3w9vQiuAY7mz+7gmtGKYnuDR+QVlNvFhdYsZsWW9edBF85XpUe2h64HXPcIBoiWF7WhZMYkOCM6co1Rv7C1v8gu4b3/rQvsHcuPas3aFRmYyP5YsIiY6Eu4Reg6qIeYsdkriYTKGGq6e1scQn0GnhC+5n+9oIxxaTJ4wy1EDpTFtZpGFiaURxK3b4dwh7sXz6eOh2NnMCbPZhJ1o/Tp1DFzagKYQaZwwP/e/u/eHb0UTGJ7jYrnKhPpoUk7GMmYggg9uCB4RIhnGKS5KklYGhJKy0tHbBqtFf3gLrSPmcCEoYRygdMoVAlknZV6BfN2eJbuJ0AHkPfip8mnuQdDByqWxoY3RaP08ZRYU2gClHHYMO6gCn70TjStOAx9m6RLBupGOaWpWSjH+GN4ZrgzeE0IeVirmNH5djn7ur4bRYwdPNo90g6mL5HgjRFRYl+DH2QKJMSFVnYGNpmm4PeH14Y3ycehd7tHfbcu9riGU5XGdQIkbgOOcqFRw2D5wBvPFz42HVLci8uzKwPqYJnQiVlI5TiA2F44OChBOFuImZj0+YzaDQp86yMcEhz7LbnurY9+AGvRN9IHYxXz1xSnxUGmADaGxtEXQQeKN7nXvxeEZ6+nGtazVo41vAUVVG5DgqLjMezhASAKLyUOOL1u3H3ru9sXinwJu9lZeN5ohdh5GDM4KZhViK741NlSWeQ6rbshLAW8se2fbpsfXIBPQVESFrLtc6rkmRURZfbmZYbvtyL3qpehR9LXrleBR1HW7iZZ1gUFFpSU05+yz7IPUPpwPy81LoHdbDzAS/lrItqPCct5dJkL+HRIfxhNGDz4dNiuSNYpaLnQKnc7LQvLzINdm95RH2pwNMEegfny5GOABJI1LUXMRlP2vAcaJ46HmNfBR8SXkrdPFtqmXyXGNSikj2OyQvlyA4E9oD6fa15rfW28q2vjezh6eynY2WaI8qijuFWoRUhY2Fd4kDjFWU7ZudpWux/LsPys3Wc+Xw8j7/IQ9cH/wrBzlnSBxQPV1UZWptYHMsd5d5dHyveoJ57XOqbghqyF9cV3RKYz/QLl0ioBSPBsn4iemU21rNvL6DtsapQJ/imF+QSYzTh1yFF4TshPWHKJAckz+c5KOJsdq5Asg914XhC/Fr/6AOUx34Kn85ckX3UWFc8mJca+9z7nVPfCV6jHtteZB2ynGeaa9fL1YZSn8/6zCDJeAVcwU++XPp1NqzzaTAkbVRrLqgT5ZlkOKMzob1g5uFiYdQiieOQZVZnDelU7DduSvG0NN84VXwkf4fDSQc7yp0NmlE6U7zXSNl3Wp/cu14Y3q6e2p63noZdvdvQWqXYTZYIUzZQKUyMiRVF00Hxvr9677dcM8swIC14Ky4nfOYQpDti3WK3YSZhGyEFYj9jW2TmJlAogeu8bf/w4XS39+a7v7/9wz4GTUo+zWCQXZOKFqCZPJseXDvdoh3rnwEeXV5V3accBtqQ2IIWGdLsT/fNFomgBj6C+/7mOuC3cLRG8VQtkutPqHll+aRLouzioGFtoQIhfKG+YswkrqZyKLdqzO4YMfp0dPfaewt/uUKQRjgJ+o1qEGaUS5ab2I6avNwq3WNeox9L304eil303IAaotlJVg6T1tChjVeJ8gYBguY/HTwqeC20YrEoLX2reyhU5q3kKeLDobDhuWD04YVhiyM6JFNmr+hYat4tjDFktKt3afr4vx8CvsYVyRRNMo/3UubWJxkgmpJcQ11RXk1eq18MXrGd5dzj2mZYqVZAk8jQtw3ripIHH4LR///7fTfr9I+xj27OK8tpIGadpNAjMqHKoibheWDsYaci3GSoZetoFurmLd7wsbQUNws6/v5EwiMFNsknjPnPp5NVVZaYP9qGXAedZF6Bnt2fih5i3Z5cnprnmBjXJlPjESfOAgrKB06Dr4AHPNT427Vw8aIunqxgaXgm8ySBY5NiTmEjILNhI+GO4qHkdCW4qBnqV6zV8FkzczaUulV+DAHnhaQJHAwu0DCSgBWoV4CaAZuenbJe956yHtfepx3M3JdbLVjUloVUKVGoTmmLBkeNBDmABTyQuG615zJl71QsG2m3pwXl2uMvIlVhh6DP4XmhWiHcZAxlTufJalBsz7BhstM2Ufpp/SwBRYVuiNyMbQ7z0guU75f12XAcBR1BHoYfWB9N3q4eKl0UW6lZHVcm1JIRV46+i8JIcgP7AJR9b/knNbUx569tLITpnGdF5R4joKJ5YXpglmDx4PYiUqNqZTVncumsbFYv+bLetiF6P71gwRAFCshPC8ZPM5Kz1MUXSRnD25ddJR4bHuHfAF8a3dPdctsNWi0Xa9UbUgrPdcuxh6FEg8EkPQ/6fPYF8ulvV6xvqipndSS1I5yiWuGg4PEhAuJvYaljQGU8J2jpBWzmbplyhDYAucL84sD3RKzH0UsaTz+Ri1RlF3/ZXNucHQidwh5G30gewx6yHM4bgNmXWGPVJ1J8zxNLogiORRnBPr3/ueh21fMA8BEsmynO5/+k+2PmYjnhvqE/oXphe+I/Y3Yli2dq6adr/a66sfw1FfjtfG/AHsStR/PK983ikedUF1dxmSTbBBzNnjueDR8sntEdxp362/9aWRgzlR4Sw08ZS8fIhUWKgjn99XoSdp7z53C5bKSqtaf9ZfGkSyL5IUthkuDPIdliveMKJGum0qj/K7Mu+XIcdRb4WnzGgGDDZYcmCofNgpDu1BdWiZldGsbcsp2h3iAeoR8d3ced/Bw8WfYYPpWG0pNQGwxLCNDFuwGRflx6hfboM5DwkW12KiBoGaXwZD6iWmFpIQzhYeEWYibjb6RHpsjpYGuWroZxYrTmuK77/T9ggvXGi8r0zYcRWxOGlvGZbFsx3LNdnl4BHxQfDx4LHZicJtnwWL2V7pKNUE4MtYkyBpcCKr6Kusq3eTOp8ActmirJ6FhmEeRwor4h2KD9IRbhSOIA4/cj6WZ96OCrh652cUF04TiVu73/EAMfhkBJtM0ukMFTu9YWmLraaBykXWOeMh8wHw4eV91RXJ2avlhL1mPTL9BYjPyJSUYpQuL/KzuXeCY0GnEdLe4qRKfFZnakI2L74bhhqqDrIWviNiKn5GwmEujKKztuAPDGM9r3X7tMfs9CwIaBiloNIxBnk7VVhVigmoQb9h30XeBe8F8bXnudtJyQWwWZOBYUE8RQvA0dyieGWILMfyA7sTeCtM9x3m4RayyozyaHZPQjbmHCYXTgnCFAofniiiR6JgSoQKttLYYxJbPH9666xH5Ugn+FjIkujGkQGdKilY+YP9p9286dJJ50XoRfHF6a3W+cWdtV2SQWllPGkOJNv0oLB5MDCX/LPFr4a7S3MbauH+r4qIKmnuST4yQh5aDoIQChfqGAoodkPyVcJ4vqya0LMP8zAHbK+yE+boI6xRsJp8yYUBySDZXYmLQZqlthnWlerZ7En3VeqZ3e3NWbIViX120UbhExzYmKpMdQg0s/6vyh+EP0xbKM7oTsB+lhJsvk6KNWojchwyF5YIbh7aJ+5Gvl0Seg6qas9TA58ox3fbnvvjGBmcWOSVEMcU+DUg/VRpedGgyb3t2q3lPeRV8mHpBdjt1wW3NZWNa+VG8RMg62iq+HwsS/AEC8mHmGNZVy+C90K5OpwGZIZUqkHqISYT8hLGEUIdwifWRP5UPns2oQLERwCzNa9l26Kb4CATlEi8g5i6iPY1JqVbFYLNldXFGdON4FnsnfZt6Z3kLdJ1uM2dXXtdSW0dLPFQurCGbEksCNfNs5tPXastpvTGyoKeinOuVxYw5isKFNYg8hTSGp4k3kLiW/J26pXex17xLzDHaFuaS9cYGuBBgIAIwuzt1SC9TAV0HZSpv83LUd5d7jXzRexh3QHKYb8VnTV1bVGlJlDxML08fQROIBQX2veYV2WfK+b5wtIGmL52VlD+SHIvthF6FpYXrhNOIq4vTk2yfZaWtsJy9y8mW1kfk4PKZAfcSdCD+K7w80Ud9UBpe2mbobdBxe3cceWl7f3uPd752Q3A+aaxeKFeTSVM9xTCoIrEUBQXA9q/n/tqIzW2/gbX6p6CcBpc7kGaKCYWsheqDR4WoiHWOwZGgnJumRrFOvXfHodON4mTyeADuD/Ud3SwrOuNHZlGAXJBks2t/chJ3Cnope9V7VnjsdBdxSmkpYDJWaUr/PBI0dSUfGNwEOfYO6GHbBc43v0mzz6z2oSqUopDWilqG6oXug7yFdolUj9aT/pl8pOGvXLsOyNrVKeLd9NT+aw6BHborTji+RuJQEVuwYr5s23D/eHV8ynxvfOB64nYJbxFq8F4UVi5KDz1sNLUkAxZTCWz7sOqE3rrNSsLPtFOr7Z1/l9+Rf4v6hi+Gk4U2hSOGVI0xkQ6b3KNCrma6Dcf+04zeQPGx/3ANSxt3KRY230P+TkFZIGSmbJpyFXUoefN8jn3peCR1yW8xa8VheFhBT4hAfDQ2Jp4Y+Qh3+fzrxNuc0o/DArksrsah0JfnkDOLPYb8g3eE74aqiKCMVZJjm0Oh9Ktatz3GU9Pn3VjwZP2pDN8YqyenM1tBu02CWsBhYWvDcYJ3O3nMerx4sngxdllxWWq4YVxZak69Qr421CXzG8cLjf317UTea9JCwwC6qKuTo1Wb6JN6jPSHdIQ1hFCC74VvjEaQtJlzoyWshrj5xenP1uC+69v8UwqLFYolfjOPQFdOS1q7YVZqQG/kdll7m3yte894MXYOcXRq4WJ3Wg1OpkKSNd0pXxlEDT/++O1W4MrRMsRBuuOuCqQKmSaSx4oAiDKEN4YzhPOG3IqKj9mZnaCKqvW1Y8Ku0X3eLOv++EcIYRfZJbAxHT4TTP9Xk2BKav9xLXa8eo58Ln3qeJx3RXO6ayZiXVrET85Exja7KF4dmg1u/xHxVeJ/1eLG7bmfro2k8ptDklOMnojThSKCoYOdhoSIj48CmYufha0KtWnCys+s2+rno/kdBrAVKibqMI4+bUzOVk9eamcjboR15nlXe659sXqWdoxy7mu+ZD1Y31CeRAE4LCzrHhgPmACi8e/jo9a4yWq7XLAQpTmclpJejiOJ3YabhLqGboi6i4WPI5bNn/erE7R8vm3N+NdO6oX46AY6FTAjFDD/PupMRlXwXqFmkm30dmh6jHn/fPt7RXZJc4pt02XSW2NVg0ZHO+gtMB/GDykB0vKm48/XZsofvIawa6ZKnauVr46diCKImIZyhIuI/ImWkAGYZ52ep2Wywb9Ny0zZKOdO97IDNxHtIGsxBTwkSrBUX18uaKNuXXNBeZl42nznevN4gXSdbq1kQVzTVKhHSj2aLY0fSxPrAZX11+W12InJ8b3FsfWnDp6jlZmO8IlFhQSEQYTdh92JPJDxlGueo6alsSO+1srG2DLkOvOyApsRnR9+K186HUh+U4xbx2U5bO5x4HdDexN6gX2Id1tzDW3bZzJdTFPtSfY9aS/GIggTowOU9I3l99hUyui/TrInqOKfApfej46KyYWogw2Fo4pBh7KNQZSZnKWmx7BjvMTJ2tck5ZH0xwFeEowgkSuaOsFF2FDfW2ZlYW8Qcw13vnw6fYB3kHkIdPVvamqgXolWRku/PGIxFSMmFHkFM/bb6QTanczcvnizIqj/n22UnpHOh2CIL4b4g5iEzImxjl2UdprRpb2uK7xByMbU+eI18d/+rg8kHzIrsjs/SKtTJFoJZLhr13FbeR57Fnq8e/14MHXfcCxquV6xU8ZLUz+jMv4mvhVpCFL5++rQ2hrNNsEgtO2oB6HJl5yQa4vNhDmDDoTJgneJHI3Dkt+avqNnrTa4VsZx027hW/KF/MgOAxqnKhg3jETzUCNa0GSja9dyF3i0el18uHz8eRl2b3D6afFgM1f4SwJBOTLWI0cY+Qja+wDrOdyR0CrD/7bFqM6gl5fmjxKLCYYthpWEIIafiSqMNJK3mAKlT6zXuDLGOtMK4JLv3v4wDHMciidnNRRCSUx6Wbxkp2yecNB2CHttfa58eHoWdYFvh2tFZIVXck0gQsw2AScnGLkLy/oJ7YzcptB5wxu5KKtToaeYVJHeijyFDoXugyyII4cEjFKQ+Jk/orqrC7kmwsHQZN546yz+fArhGzIpDDMDQ1hOG1qPYStp4XFtdBF59Hp+egt5AneLcvhriWLMVyJP/USHNrkoUR1sCqv72e0A3/zPicNZuhKsTaKymuGPd4uHh32EfIMrhTOIiop9kUiZgqAArUO3q8Qzzp/dJ+6O+nMJ4RbdJ/IyVELKTEBXUV/Haslv43HgeOh72nw8edd1r3N6bchkdFxtTw1EOjj4KK8a+gyR/mrwuOHh01rH/LrjrlylE5uZkk6MrYYGg3aE0YM6hqKL1pGdmUKhDKvqtfjD6s9J3qnpNfieCd8VKCWxMMtAgUs1Vw5iTWjIcWV1AXlQfPl7yHineEdzfGwOZPFZpVN6Q583OCkoHZEOIgEN8THjEdQDxu25uK63pqeYcZRUjbyHwIU/g2aEdYZli72OsZecn8Cp1bNiwcjOntm06VH52gahFJ4kgzHZPZdJ3lYEYN1mWG9HdWd3jnnce+Z4zXY4c9ps0WG6XClQ6kXpOfgsRR8pD64C5/DF46PXOMkPvXOxZ6XOnQGXno1ri/+Fk4QghFuGoYq3j/KWT6ARqDqzV78Ez1XbpeX79soF0RSIIoEyfz6aSupV/10cZuhwOHNxeXh77HxafDV3fXTxaudmY15RUTdHIzsPLZkeww4YAonz7+QJ2AvJsryjr++lzp7/lQCNm4kuhcyD34P9hSqIpI2glsicRagAsqm+Ussd2OznMPTDBEAThSC3Lj48rkgkU0ldCWeBbqN2xHhsfUl93nidd313Jm9qZjZdE1KKR/U60C30H3cR/wNR9Gvmntn3y0K+DbLXpmGfapXWjo2KWYUEhMGDR4Q0iUaP55XtnTmn8bCYvvXII9eZ5Y/1sQLMD0ogbC2iO0RF5FL1XR9m922/dZB5s3sMfEV7eHpQdbVunGaDXh1VM0kuPjExuCFIEg4EBPet6IHZr8wLvz6056d0ns+W0I/MiF+HJoVKhUOI/IorjuKSDJuCphCw9LnLydLU6uMk814CORH3Hq8tRTvuRZJRmVyvZANvwHFedrd4E3s3es13GnV4cKhnSl1oVRxM/D3jMFQiyhVRBkj4pek/2kvNWcEotaerUp9tlhmQR4wSh8WFL4VChn6IKI7dkkabvKMpsXO7SMbA1MrhfvJV/ssP3h7FKVw110PRUYNaRWPKarNyxHXkd5l8znmqeEJ1aG8Eae5f6VavShZBFjPLI2kX8QS5+rnoe9x20ATAgLYRqtmfQ5enjjqOdoWQhRWF4oQQia+Mc5QCmzyjOK/Iu7XFidHT4Yzvqv2nDIwcgShQNYBFzEwcXeRjX2uNclJ2j3oNepd8EXrmdR9zfGr6YIBXLUslQYc14ibCFe0IKPtI6XTejM+fxLu2VqtUn9yWRJAsi0iI3oPtgyuGJoZOjHmSeJlPpNut4LmDxVDRs94D7976Ggk4G8wnIjSDRNdPt1uGYXFrEnGEdz14OXvlfGF4Q3YjcZNr12CjWkhN1EHSNAMluhi4CU/7Tu3v3gXQesLjt0ysWaHnmXORQYwmhiOGjoWMhoCHtYtUkpyY1aKXrJS4EMXD0Tfgeuz1/I4KkxlFJiszU0IdTLtXrmFUZ9tweXU9e+R6kXySeeB1X3AeaaRhVVkhTp5Exze8KUEZugiH++HuGODV0dDFCbkcrWekbZnAkpuMxIlphKqE2YRJhziM/o8AmhSjRayMtw7Cv9Fo4AzsvPs7CHEVcCQeNVlBT03BVzhgJmv2b/V3EHqyfQp833n1d89x3WwFZJxXaU9yQ4g4hCrsHIIMGP0R8BjiWNIDxpO6H63oozCaVpJkjuWIIoYXg+OGvoRfi+ePLJfPn6mrfrb1wMzMstpC68755Ah/FzAm+TOEPppLKFatX4dp52x5dXV22XqCeoZ5SXgucpFsHGSOXIlPT0d7OGkqKR2RDt39J/FP4qHWAsfCupqw16Stm9WSF5BMim+FnoPUhFeG8IuIkZeWi6BGqY2zfr+NzjvYwegM94sGyBZkJOMwuUAJSjRWbWFXaNhuI3aWecR7XXoveox3dXMRbAllIl4lVAlGfjqaLJkcbA99Af/w1eRB1znLerrgr5SmHZyIlnqOwIlXh42B4YTFhomKEI+NltKeNqgFtBa/JM3j2QjqpvUdBicUuiIuMFM+qEjTUzFeOGdwbu5yInoceiV6AnqleJl1A2tHZvVcjlSgQ947LC6RHtQQSQG+9HzlAdenyLO/JbDapGybcpaMjueGN4YZhdeEE4ZCiVqOU5gsngmnTbLzvEDL79nC5qnyGAfQErIfQy00O5ZIZ1H3XBllLG4qcXp3Eny4eRl7a3gIcwdwxWYpX0VVPkkoO3EvRyBaEykFgvZ55f3W58hSvbawk6YeoKqViJDXiaWGdYQghAqFjIeMjTOVk5vcpYSyH73nyQDVhuRF9agD9hC6IEEujj0mRyRSBlzpZOhsznGQdSB8cHwCfX54MHRhb3to7122U0lI0jxiMPwj+hRUBTf31Oiz2sHOtb7ytNuoA6CTl4aPqYqNhiOFYYWuhGmH243skyac4KNOr2O7jMcL14rilfBlAJsPsB6FK/M68EVnURVb2mQ7bZVzIHYJepV5yXndeZF0DXFsaXBfV1cZSYxAby98JKoTDwij+VnqFtzHzG/Az7XpqLWgp5WekPGKEocUhgOEuYLHhqKN+ZK7nFqlRa5kuaLG19U54h/xDP6dD5QcAChTOFxFwk9zWUlhVmwpc4B3m3ohe6d68HgCdptycWlPYQ5XLUyyPlwyIiQNF8IJA/oQ6oDfxs7+wmW2tapxoRGZAJA6jJOFOoXxhN6EG4ksjKaSIZqhpv2uwrrNwwXT5+Hu7pz97gtRGmgpBjbbRD9Q6lhRZZhrQnLYd4Z6KHw5fM56QXdgcKFr42PdV8xNIEEQNnwnaheiCXn74Opl3LrPvcJLuQqou6F3l1KT3ouHiHODtYLwheKGXYoGka2auaRXrJK6nsde0i3h3uss/TgLChoqKg82YEJVT/xX2WN8arNvTXgSeqp72Xwleil1EnAmaGFhh1fdTQdDNTT6J70a5Aoy+sjr5t/A0JzFF7d0ruifmZlnk/OLG4cXhoqG04NqidSNAJIvmLOica37t1HFuNHb4X3swfsKC1cY8CbfM9lBqE0XWZFfo2rmbiZ1LnmAewV8THq4dSRyWGwOY55ZUk/oQuc1qSocGboN8/xl7/bfZNP+xZS5X67Io+WbAJMgiSKIA4RyhLSEHoUqiv2RypU8n6Wrx7ZKwLbPndwH7J35ogqTGA4mHjPDPgdPylVoYitqqnCddft3jXqHfQZ69XdycGRqtmLoWYpQS0TpNPUpBxtzDtv9mfC74XvTFcjkumGti6WOm3SUJYxHiAGIcIPbhL2GO4q0kJKW8J/MqZe2isOEzm/dHuqx+REF/Bf2JVYyyD4UTYlWdF5+au1veHXLefh5LHxWewN3IXRabIJjEVxcUZ9HrjlvKvseGREHAKDxW+SN0r3J77pVr66mE5zDlPyLvYlhhGSEjIdBhuWKfpCFlnOgO6kwtWu/rs0122vqxPbjBW0UASOvL9A+fEwdVABe6WdRb710fXgye017k3pGemR00Gy8ZVBc1lGiRu841SxqIAYQUQES82fkzNVlyC+80q6ypCWdnpXYi3KKHIa3g6mFy4W5iYGPJphAnfOnkLVsvrXLRNrA5dn1ZgLREpQiiS4+PQZG41N5X1FlNG+sdQJ5x3qoetF85ndEc+FtD2QoX8FSGEr0OoMu7x1FErsDdPQr5hrX3MxBwOuwNaU/nXSWSpCciU+GLIQLg3qFo4lhj6KTtZzNpWyz+LmBylnXf+cp9OsDbhLKIUQvnDvVRs5S8lxKZ19thXTCd6t6c3sTe6V3N3GVcE5mol8WVVtHgTscL7shAhYuBVL0teb718XKvcB1sxao9p9hlieOZok8hqeCx4TuhauKuY31lB6byqVAr7y7z8gr1mvlEfJ1AtkNBh86LRU7ZUjxUY9c+2ZIbFlz+nZgeLh6AH0Vech0U24BZuZe+1L3SfQ87jD1IrMVcwZT9+jn6dusy7LAF7QoqHufOJhLkYOK+4U1hE2EI4f7iYGO/pOimVWkkK/nvFrFgdVJ4pf1TQD4DGMdgixNOENG3FD3Wn5nMms8cyB4hHp5faV8U3gVdYRuPWcLYR5UPUymP04wZCI9FS8IF/jT6bDYkM7owam10Kvcn0aVLZJmiqyIvYOqgyuF6oavjNKQdZzAopevlbvXxT3UmOI176b+ew33Gycsujf7RfZOuVpAZcVr/nEnefl4lXk8eeF4jnYfbvJqsl/4VfdLmUDJMoEljxUACdL5VOvx3O3PLcXntearp597mHOR0YpRh0iFyoUeg4SK0YxwkzSa36N0rGW47cRC00Tj7e+u/fEKWxmoKnI3dUQnTvVZcWVsarJxIXV6eoR5x33GdmF3u20Pa49jM1nhSsBBnzPTJO4YZwjv+vDs1d3c0MPCgrd5rdujY5j0j5yKX4eQhXCE04Uxh76NPpNtmQCkD64YuhrFINEE31DuyP1DCyEaQyfnNH9BkUzXWR9jnGnbcjR3enlreu17dXledr1u52pTY4NYw0/JQJk2TCZ7GgwK+Pzi7FLfddDIxcu4oa5SoueZhpMKjdCFaIYGgp2GQoQkipCQOZjQoGKq5bZrwkHRVeDz6sn5mglOGOYnoTMBQ0FNv1ZTZGFpEHAYdfp3sXu0fNF5l3Y1cgBr2mH1Wk5QYUQbNnYohBoCDEf9k/Az4fnSg8RtumasjqPemDuRGYxhhUeEvISQgxKIhYqEkBGZMKDCq5O1h8MHz7fcY+uk+lcKjRdXIxIxO0C1TAFX3F7zaXlx+XPTehx7pXpge+B29XP6awpiHFsBUuhD0jctKkQaGA73/ynxguO31UfHZ7k8rp2k25oFk62ORIhZhGuFGIYOhdSMsZBVmZSfHqqctEzAms533mPr2/gWB3QWMiQTM5A/r0twVpBef2p8bod2ynecea987XmxeJJyTWv3ZG5aS1ASRdQ6NC1tHqMPVAID8RflBtYfyfK8RrCfpJGdrZPGjNmIEoZGg+qF44ayiZuQrpTXntOoZbBLv4nMWdiX6Sn4cAhYEiUhsi+0PYdLA1VPXENnKG1NdWt5mHlhfY16+nc4c/VrtmegXLVTRUX6OAkuxB5rEL4AQfGm5AzZRckWvY+yVqV0nUCW7Y2HiSiGFoSBhPiHZ4n6j+GV9Z1SqPWywryEy7/ahOfE9cYChhLGIewuKDqUSmlTY154Z3xtOXUeeAh7An0Te5124nM5bu5ma12HU45I3jsmL90gPhMvBNX2IOWy14jLCsAhsaKmd55KlSqPX4g3hd+E44OIhWeKco8sluadmai1sSC93sec2dLopPT4AkwSHh9ALvs5W0fTUXxcgGb6b5F1s3aUesV9CXt6eF11eW5sZdhcRFZFSZ88fy4YJJATGQei9obnF9lWzSG+ZbRtp4uerZXpjkyLzoVEg92EOoZRicyMpZRXnGOlM7DivfTJ09ZE5G7yvgNFEHAhlSw3OvdEmlTbXKlmZW0ucg14t3nReQ57Lnptda1wQmeWXxJUM0ekOzE06SELFpIEmfdE6tna+sy1v7a0y6c2n3OW2I6migqIvYNehMaEL4mojcmUW5rGpuCuW7wuyNfUxeOE8Of/mBDiHU0sMDluRStRF1oMZcdqGnSUdlB75HqBfQZ4z3WBb1Znfl8YVaVLakKHM0AkUxfFB4b5HOsw3MfOocGntEeq5qE4mQ2QGYtohkSGeoRgg12Jz4pek0icM6Yurzy5iscY0oXgfe8nACAOixuJKS03E0aUUhVaaWPTaQNzRngee9x7ynyWejh3IHIQa1BfJ1fgSsk+bjLEJeUXdgcK+qHqv93vzTzDFbfpqRufu5eJkkOMFIrAhCiFyYTIiceMppEDmrekLarStqnHM9RG37jt3P7TC9AcxikeNUFC/00gXONh2Gr1bvJ31XoTfA56C3fFdEVwEmzTY2xbKk2iQRI4aymWG7YMTfw+7sHdotDoxK21VqsfoseYmZEPjciHDoVDhZeFV4iajpGSwJpkopCrCLgTxHfSSeC+7Dn9VQkaF6om/DVdRC1N1VozY2Jox2+OdTx5uns6e5l7mXR3cZpraWT5WEtPk0QmNPsl/xrUC838mfEs4f/R08F4utmt6KGll3uTZYw4hp6FGoRzg22HaowJkO+ZIqJFrFG4XcKN0MTejupz/IcKJhjVKYkzrD+uSpJXcmB8aBZxRXdIetp5hnyzfFp3MnKzaxJjjFn8Tu1Duzd/KdMcuw6y/4jvjuEi0uzFq7kzsNCi/pjvlIGL3IichnyFLYM5hmmL4JEsmJmhLqzltV7Bw88d32fsV/jrCVAYFSRUNTFAa0tgV+9e32avbxh0iXmUezd8sHvIdoNyh22wY8hcPU7GRbM5rSrQHAAQa/x98Gnk4tRZx2u8ea8zoxydmZPsjViHe4Y6heyCT4W+iiKRQJdfoG2pqbKMwb/OXNpT6ED2Lgm1FVQlVjERPqhKRFWYXNZnVm8+del50nyjehF83XbFcUdstmIVX3tRJ0fzOnstzhq/D6UAL/IO5LrVhMi+u1Syx6MInWyUQY9AiLSGBIW1gxKIm4ytjwSXI6D9pnu0zb2BzYnayejO980A/BIxIk8w0TzpSElUWF4ZaKdsRHX4drx5eHz0eRF4HHTvawtnu13hUhlHeDv/LSAgaRHnAc71aeZf1gfKur55spOnUJtxlMaNqYn0hFWEEoZMhTaLp411lAmdi6hVsxK+08tG2iPm1fUtA0EUMCMCLvI7HEnXUiFdmGchbphzhHdPead5DXqReD9zPW55ZIRea1S6Sbc9QC6iIcIRdgQe98flsdoCyzK/zrLJpXyc7ZbdjYSLd4crhTyEM4c5iH2Q2pSmnzOnW7F4vzTH89j74/L08QIvE2gg8C2ROvVG21QXXo1lQmoKcjl4BXlye4d503kSdQxv7mibX65U1UiiPUsvbyBTFGgD4fW86T3b5MsswKyyZqkMnsWVcJFGiu+FQYU4hYOFDIhPjiCTZ5wCpwSwDbyuySXXyuTw8yIBAA8qH9Eplji2RQ9S2FmKYwBr1XIwdwV6C3t+er16v3UScQlp1V9sVVFJoD8BM20ihBNzBcf4/OrQ2c3NMsLutSqo2qC9lgyPbItJiByFjITphPeJ5YvKlNKcHqYnrxe9fceL04jkZfDVAIsP6xkgLKE6PkTSUbRcC2UGbV5yanbEeCh9HH1ce690JnJtadlffVdiTIc+VDFGJCMVoAjx+A/rSduxz+/AQbUbqx6hwpeEkMKJM4bGhPqE0oJ4h1WONZLImQCkZK4Xu5/EydXK4dHwXAD+DUsadyc8NW5E1U6gWQlkUmyAcelz2XqPfF18wnd4c1lwP2pXYZFWqkqTQYQzxSciGfQKQ/ne6z/dxtF/xEa3pakWo+GZK5DTiw+IKYUbhXCDHolGjqiQV5uVot+sD7gBxU/U496B7+b84gs3G/goaTakQXdOTFivYtBpfXGedZd6J3wCfVd4QXWpcPNp3196WDxNUEJ8NGkmjRiTDFX7k+8C3w7S7sVquPus26LomE6UG42ShsyD2IS7hLOIBo2nkreZyaKOq/i1ZsZ20dDecO2C/FAK3RryJmA1WEIrTbpY6WIIaE5xBXYQeEl9OHrFeYN3HnDaa5xixlkAT4dA8zX+JxQZwQv++m/tLOCV0urDoLofrdCkU5vakQiMDIeZhTCDqIWhh+SKdJI1lxGhh6x4tRzDys+t36zqsvqLCdgWzSSuNLpAbUrwV+9dj2oGb7V3eHv/e5l7QnjqdbpzzGoIZR9ayFBYRqA5eCsaHGUN7/3i71fgE9QAxlC8K7BVpbmZ1JTijNWH1oUShVqF24ZiiimPZJcwoL2pjLfWwvTNxdvt6sf4qgejFS4lfjNoPi9KslTaX7pqmnB7dX54nnrNeT15EHlTcZJrUmVmW7xPSUa3NrYrQhw2EQQD/PC7377ULMmlur+xLKXIm2eU4oz0iO2GXYSxg4yF/YoHkEOWRp4vqSi0UL61zLnbFulU+XgHRxRBI7QwcT2WSdRSD144afZvGnaMd6l68nuFewh3iHFRb/llL1zZUCJGUDjEK+Qfqg+f/6b0FuSo1EbI0r2SstGk+pxKlDGNR4hxhoaCZYNIhgmIpJCmlg+eFanQs4e/DMt02a7mjPe9BcATvyDHMfw7kEmXU9JdOGcicC51WHnAept6x3t8dwVxZG5yZLtczFBzSII8vC52H44TugIF8sLkuda6y5u+RbPMqQieN5ccjmqIuIk1ggGDaIhaiZOO/5O1neOnk7E3vn7M7dik5nb0AgRCFFYkhC33O5dKdFJRXX1lfW6RdCJ5RXpUejJ7GHo6cWFuyGUiX0JTRUepO9stTyH0Et4DW/UV5/DZjsxNv9axMKkunB6WzZFdixOHJIRzhfGFRYpokJeVrZ5epfmvKb11yTDY1+P48+YDxxCaHUot+zjVRkBT5VxgZpNviXPYdtR7WHques93UnRfbnJoWl50VUBMRT1BMWkjVBLnBbz2ROc027nLq79ItQGnSZ/ol8qP7Ib2iDuCv4O2hSiHSYwekimbE6c3sem84Md81/7j9vUcAksPThzbK6862EVTUV9bImZSbJVy13Ueesh70nuceWd2Zm8zaPZf9VViS8ZAejApJOUVvAgF9zzocNs4zZTBobUxrFKi15fLkbGLiojIgzyEcoSYiYSMRJK1nc+kl69SvJLGfdSm44nyQv/4DSYbXyhfOBhFj09vW81je20Pc2l2WXu+fDB9BXivcz9x3WdwX5JWfkuwQdwzCCa+FugGsvlW6yvdts90wwa2Q6l/ny2Y5ZFzi4KEhoTwg66G5IZpjOuQp5gmoieuqrpQxN7TTeI47k3/jQy/Gl0lAjmMQz1RWFkmYphqaXNOeLR4D33Iejh553UbceNqDWDGWD9OLkEgMjApXRd/CAf75+od3bXQP8IVtgCr5KEUmLCSHoz1iICGw4XxhJaGsIkblGiYxKF0rd+3ccXc0qfese5s+6IKbxkRJyo2K0K3S9ZZ7WISa6dytnZzeIN5onpTedR2n2+Ja2dj2lmYTS1ExzOPK4YaaQyy+2XuAOC00QDEarfLqW+hKZonkXGM8oeEhi6EbYXliN2L85Hllyij+qyfuN7E8tDk3fnr8vo0CTIZlibuNb1AFE3oWP9iIGtAcep3cXgYfdV993lPdvFwbWyZYeVYAk8oRHI3OCkVHNUO2Pzl7ureWtRSxDe6wKzApYaZOJUMjcSGUIQZh2WFEIeCjNiRH5kGoYmr57a4wnzRDNwO7ar5QgfZGbQlyTOJP6xMPVamYNVppm/MdPp5oHpKfFp4KXkRdP9pXWORWohRc0TEOdcqwRzZDXP/hvCQ4AjUNsmsuMurPaRSnSKUIY0UiNSHiYR7hpyDtYmNj3GW/p7nqja2lME8zerbo+nk+RUHOhW8IXsxV0CrSh9VR2AXafZwtXPkeCV7zHjNeTh2YHPta7Vix12tTylG/TglK1AeBxAfAbbwdeLg1TjHvbr7rsqkL5y9kzqPgIeshDuFKIR/h2GMzY/3l4qfMKl3tBbAtcyQ23no1vYVBekUQCSLMfo93EjWVPFdZWc/b791Snd2er15vHqOd4BylGurY3Nc9FL9SEs83yw/HlsSjwJw9KHl3NQtyCm8dLHRp6qcPZQpjkSH54UrheuGEYTJiEGPlpScmxWolLKvv3DK3dh55132tQRkEzkhty+vPHVJ3FLqW61m324ldEZ4KnmAemt7VnXKdNlvImcgXT5TVkruPS4uSCAnE9wEqPWO5gnYaco0vteyL6bCnEuWg44Giu2D2oW6hguGs4dLjj6Uf5w2qLiyZ711ys/Xk+bu9KcEDBF4IYMs4TyrSHhU3VyoZvRtlXUFeeh5k3zzfOZ5tHKtbfZlMV2xVaFIgzqXLpIiUxLEBCD2m+jq2knKMb+ysPapGZ6zl0ONlomehd6G+YNqhkaJ8oyylcKd06YhsBC+Lci41i/n7fM6AakNlh21L/84hkQDUn5aUWW9arZ0SHcIe1p7l3rseVhyE2+eZzVeZ1XPSVY9zy9ZJNASuwVW9prpn9oTzPi/ILMsrNeeNpVTjRKLPYaIhsWD+YVViMeLdpWemteioK4juvrGHdXn4aXyYADeDgIclyhGOTFG5VCoXMhkvWxNc/F3dXrVfI16vHrLdO9vMGkTYDBYGEzXPhUwOCRpGcIE8/r86b7dYc2GwgSyI6rFodCYg5EijNuGYIVTg7OF1oeDjL6T/Jq1pNKwgbvxxmvTIeMk8LoALAwFHdAomzUgRKNRBVmTZflqUXEGdmR6SHxee3R5VnbBboxp3mBxV4tMTD8mNJ4lnBSxCBz5tuzu3nvQOMO+uP+sBKH+mT6Qy4yKiHOFxoOPhA2GrYzOk4KZz6HDrd64hMTI1GffwO6O/tIMcxqZKOs2fEMVT0dZEmKua4pxpHSQelp87ntmeAx3hW7GaUNjzFdkTZRCHDPzI0sYXQkX/a7u+93X0CLE9Lc7rmqjZZcSkhuK4IbMhaGEc4XUhvaI+pCxm/ugEa69thPF3dH+3sfr9v1oDGcaaCgHM3NBYk+XV3tjOmvFcWh3XHlbej98KXfXdidwPWw7Y4lXO063QQ439CeQGNwJ8/ul6xThxtQ5wy22Dq6uoSqbv5Pji+uHFIVjg86FqoUji+6RzpkUnxWsDLb2wrPS7N/F7L37XAnKGL8mLDOWQdNNXldeYY1ognAldRF5RXrFefB553UVczlqEmSbWrdQiEKcNgAsfBzrDRYAVO9h4unS5sPbus2sPaMPmnGS/otMiCWGwobUhJWG0IvgkJyXT6EXqja2q8HC0DreNuub+okHThYnIxo1aD61S7pXQF+sZtRwAXYseRR6vXnaeLZ3THQ6bU1iI1tzTztGiTisLFgdZw0GAczxJeSu0wzGVLwergOkHJy+kuGMy4nQhkyDVIT1h72L342wl12fhat+tGLBHs7n2+Xm3PWZAr8ToyRtMg49TUqEVsZga2d7bA51bXi/efZ7VHySd7VxuWpgZQ1c4FGqRdM67CynHAUOtAJn9HDiEdX1xyG+N7CAp6+bvZR6jiaGz4Yog6CER4QriSaSMJcsoMCo7LE5v23MsdeK6t33HgRMFSgikC9HPaVLRlVPYDJnQ27jc/F4NHw3ezp7a3hUc+JszGPNXGpTEEUPO7cucCDeEOUBAfRh5zrYKMmxvfexOag6neGU846ViU2HNoTYhvKGI4qvjKWWyp1aqmqzHr3VysjYqebj9f8CZhMrIOYweDuMRxlVgV5VaEtulnRKeg571HtGffd48HRLcLdo7FzoUk1JDzwYL88fkxPuAmf0yuVe1gLLs70tr5mnU6CKlxSOdoenhq+DiYP3hryJI402lNWcVKaTsM+5t8qx1+7kq/TnA/0RGB5NLOk8lEUXVBFcTmeHbqR12Hc1e4l72nm7eOB0enAOZhNhg1ZUSsE8rTExIcESlQSV9aHpvdm2yuq+rrQ8qvCe+5jUjjiL/IbnhD2Ez4WliByOKpU2nKymbLDHu+rHJtda5Xv0oQGLD/0dPy3oOipIx08IWkNjmWyQcXh4iXpCfWx8fnoEdTxuLGgrXXFTKUpgPvMwSiNZFlUJofUv6rLZgs2CwFe0NKmtnx6W6I5niZWIboT2g2qGx4dvjECSM520o26wZbtmxoTXueJM8hEBTQ1qHVktXDiaRG1StVxjZGBsz3IadEh6znuVeYZ6anTVbxZolGI1VRZM7EA0MZcm0xbqCPb6+un+3FvMnMITsuiqpaGMmv6Qu4tNiJ2E7ISEh6uHXIwnlo+aBqREr6m5W8V+0aniDvHS/noL5RwEKsM0pUNVUE9YVWWObWdvM3lpe+95CHxnecZ0pW9iaXFhr1i5TARB8TGDJxkXpgfe+VfsCN5LzyHC3LXRqZihsZnNkZqKa4Wrg3CFn4VghxWMwpKrmCaiP6xpt+zEfdJx3rDsSv4FD1sczimxNlBE8EyuWqlhY2mKcT13HHgVfHB7pXpbd1FznGvTYspYTktxQUE2KCdxGcEKWfuB7fHeltGEwzu3HqyIo4OYiJMEiWeJY4Ujhc+CwIeljHWQwpcho2CtPLYpw5/PPt7y7638kgxjF4woLTamQQdPuFcjXx1rSHLwdVV5SXoVfKR6m3Z0b45sD2OkWWdPekThNngqQhygC8z86e303drSf8Zfub6si6QkmiWSfoyliWiHl4QAhwqHCosUkcSW96D7qVq3OsH4zrfcA+x5+ssJORc0Jm4yVkBjTB1WPWJ9aWRwEXaJdzd9y3rFeZ53zm+2aQ9kVFyaUKZCATluLOcdvgzU/wHwxeDw08vH17rUreiioJuNkn+OuotAhlOEdoXVhnmLupB9lh6hWqn8thnA48u42y3rgPjIB7cWRiRTMW8+fkpfVOdgR2nbb/11GnsfetB793faeL90ZWzvZGxZrFFmRs83cyu5HagPef/C8MfjAtanxtW6bLDmpHOaFZSCjiWIhoTKg5KD3IV+ig6RcJafoPuodrarwL3OyNyr6J75ZwfrEy8jkDGlPLlI8VNFYRRoEm9JdFd4nn3pfb16jnVLdLJtwmSYXdtRqEOJOhwsQyBTEUcAKPLa5PPV3MmYvj2yi6bAoDOW4o75hliH3oLcg/KFtYoNjqmYc52/qG2xIr4gzaHan+eI9QsE6xNzIkwxvDzzSmNUal9NZ1xwjnQHdx58yXw2fFx4L3Kna+9lnl1OUURJ9zxKLRMhFQ9aAmvz5OU+1+/LgL3Zsq+nxZwUlLaM9oYKiDSECYUGhYiKgo7flYSfj6fQsp2/NcvV2EfnTvRAAT8RbB8+Lj0810bvUgNdtGWTbedzZnnxext7An2BeK11JW/vZQde+FIqSTc8wy76IeUU9gPS9pznbNe2y8S8JbTrp6KgdZRyjk2HP4YthCSF/ocDiU6OkZEVnRym2bJgv6rJQNZQ5N30YAFmEE4fQi7DORpIelPbW89nnW74c7d3dHoefGl6sXlddFpuk2fpXV9VqkmXPfUuWiQbFBcG9fQ+6ozZBc3xv6C0Q6nwn52X047ZiGOGuINHhdqFHIcAjQuUcJz0pEOxg7x3xr7V7uM28uv/nA6NHPYsdDjzROtRKFuSZVxtEHXhebZ6G3yae6t3anRxbzNq2WFeVAVMlEB2MsoisxOBBsr6merS2sDLM8Jps7aqUJ8smJ6Rg4r2hQiFz4LBhEOJoYwHkzGc9qI/sPm5LMhL1YHjIPEn/18N/B4RKQA5NEXaTmNa/mQsbENza3pffad7CnwCe8Z06m86ah9gAlebTdtBAzV+JNsVQgeg91Ls3t3sz/7EZ7imqbafEpjjj2eJaIaGg8SEroI4hzqMmZTUmXCnWKyeuZTEJdMa4IvtYP9VDrAamyfGNH1BO0/HWVBjCG3ScVR54noHe817FHv/dS1xx2ioY9dXXk6AQm81piZjFjILsvmT7bnhJNDiwne29KqhogiZfJLPjAyHAYT9gaqFPogPjYKSlJgwo4+r17agxCfT8t7V7gD82gmRGWcnnDf/QO1LTVg1YlJqq26wdZB573pLfDF4wHdobRFrhGSCWjVM0UFhNR8nghhGCzf9Z+ws4aDRZcRHuh2toqEWnNeSHY23iYyE2YKegjqG1YupkruYR6Eaq+O38sT20DneI+1Q+lsJ1BaoJ502gEGYTDdXlGBgaOxy2XSaedZ6a37Rep11Z3KfbKZjvVq9TbNEUjZBKp8bHQu+/VTvw+H90UHHQbe8rDSip5jJkkWL0YhshtWEToU7h7GLr4/+lV6gfqsgt7zEq80x3zXpwPkQB+YX6iZaM8xCCUyYVpVjImgucAt2UXqReg59PnpPeJRzK2oZY3VY0VC3Q1Q5ZitrHBEMPP/s8UbjrtNAxbu6XK75otCbpJFhjqaIOIXVgXSG+YbUipGS4pZ0oNmpsLQIwrTObdxt66L3mAjKFoQkozJrP7FLN1cZYg1qeHD4deh4EXvffNZ66HUXdTNqh2ZjXDVQukWqN7QsLhzzEM8Ah/Ti5aTU2saAvHSu7qPonB2Uu4/iiQaGs4VhhqWFnok1kqmXX57rqI+0CMAszMDZ5ugE9AAHYBaLH8ovqj3bRxNVWV4dZ8Jvm3dDeWZ5rnl7fAZ59XKBbJplq1zAUuBGjTliLNEe4RCLA7/yNuXp06XJ9bwksVKnxpzfk62N1ogXhrWE0oQdhpaJoY61lWaetajTsmu6lsvK2WLmLvQ0BT8RDSJQMMk7j0cyVTJegWeBbdNxv3Z9evx8Rnr7deZxxWwhZQtfDlJLRy07Jy1LH4USHASC9O3lqdkAy4u9wK+Wp/qeKJdQjtqJbYZhgo+FcoeIiJ2PDJhpnHKptq+YvY/Kr9o+58nzWgR5En0gMy1YO79H41IxXjRnLm3YdBN6nXj9erV6Lnj8c69tRGdPYCBUL0nWPDYv9CQbEx8EkvXC6BzY2c6tv/iwgqe6nCeV64xLiGqGkoMRhQKFSYlxjoWUd5wWp8axEbpKyCjXzeTO8mQAnhGSIQAumzz2Rv5S8ViXZEFun3QEd7J6tHrgeCd6t3WAcKxoU17EVVlJjT0kMlwjAhQIBUT4quiA2SvMSMD1syuoGp+Vlp6OWorMhxOHpISSh7qLrI1qlBucWqT4r8C8gMiH01PjL/Gm/agOzx6xK4s6z0V3UmJaR2SVbeV0C3kgej59t3qMeKN0YHHGaqBhV1ZLSjg+qDLiJAQVJQds+HjqU9sWzJLA9rdaqp6fdZgKkEmLGofzhbeBHYeniE+P5ZIynFKkQa7lugvI59RO45PwCwHbDW8ckChhNUNDAE97W5Nmr23Fct93fXc7fDd7e3qAdd9v+ml5YHNWEUm6P8YxoCZEFu8I7/jq6yfecM4QxKS3+anUoUuZ6pD0i7+GPYMEhOqEiYnajKmR1JmYo5KsirqkxLLUs+E88JT/yQxHGc8mGTYwQVZQy1tvYuhrFnJtdXB8WXv/f7l63XTmcMVqEWOlV3FMdEMoM6cnMhioCQn7aO1s3LrRt8P8t6Wtm6IQmWaRG4yvhyaFfIRzhtmHoY0cknaWUKQprbK25sSO0CDiWOtN+ykLPxh4Jxs2/EINTv5XF2J/awxxKncBdud8ynzLeod4znCIay9kXFj3TGRDRDTJKCkbkQ1c/K3w1t5p0dzDpbdZqkKiVppukUOLU4bxg5yEWYVdh3+MnZJHmGah2KuBtlrDCdIh3Vbr4vjrCmsYDimhNeVDi040WsxhUmmsbrp1WXqTfeN8GXuBdyRzI2w5YhdZuE6vRHQ1AyrGGdYOyP7U8THhLdPZxGq5xa16owSaG5PbjGGIVISGg2yD04ZSirqRBJdiohWqc7cHw1nPSt286r34uQhuFrclnzRrQfJKu1U/YW9qQW8rdt16q3o9fdF4S3eRcYBqF2QzXLFSNELYOUIrnB1MDwcA2/KF46jSLsd5uwmwNqPrmg2StYwyiGuFIIRqhZSGe4oRkOeVqqC7qRu1gL+8zqjZ1ein+goIuRWwIRAz4T1hSuVULl8yZ5ZumnKaeCl6D3s/eoN4CXPpbGRmIlx/UThGujutLGwc+g+8AozxTOPy0+7IZrsIr+qleZ6xleSNzonihh6E0IQ3haiI4I1DmH+fx6pFs0m/Vcx/2tvng/eKBVoUpSDaLnI890hEU/Jg6WURcKR14XiDelB6a3lwdq51B22yZ8ZfG1SFRn86Ai8EHxgTFwHs9Dfm3db4yTK8VbLmo5mdYpdsjlSJE4e6g9qFD4Wdic+NdZWWnQGo77EDvzbMftgA5zX0VwVAE+Uh/y1uO1ZIrFI1Xjhob2w0cuR5k3oyfkB64Xfgc7JtuWdpXR1Tz0gLO3wvLSM7EQ0D4PQA5oDZx8k8vhWxYqjInEmUsY5rimWFZIYChCmG7oqqjnSUjZ6bpyyxBb5dyn3X9+Xw86MCdRNXIAguMznSSMtR51w8ZV9sWXSXd/N5BXooe5F5IXQEcOZnG2BQU5BKRzxaMZUkchJ+Bnb3X+hv2bvMfL/1ssioXqGJlfaOooo4g+KEV4QZgyaKBpCjlZ+btKhMsZy70cqL2APhC/H3AvYO/B6DKyU66kN8UYBasmVSbnlycnYVfGd6On2yd91yDG6BaZVdf1VHSKg+QDP0I80VnAVa913o/9vzzafAErRYqtefYZjOj46KqYbShPyGuIRgiFOLwZGWm1+kHrFJu0bIkNME4tbxEQDGDxoeEiuzNSBH5FB6WsVjbWzRdJF373uOfGd8THjfdOxutGVfYwlXHkyFPuwxFyMxF8IGnvl56/Haycsawsq036lUnoyZKJMsir+ESIdWhC2Ey4h8jciTcJ3RpKSvbLkwxibTY+N07yz92A48HMEp0TdDQthPPVvoYl9pIHMmdgF6a32FeQJ7AXbtbn1rDmPyVplK10AyNCMm6hd1Cen54+uu37LO+7+ltg6q76AgluqPD4rIh8uEt4cTg+6JlYzclc2YK6RVrtq2VMZJ0sDgde6x/VMKphlYKak0R0PQTY5ZS2JgatRyXXVzeZp8UXwwec11X3Eva/ZhqlhnSwBAezI6J0sZPgtX/FHt0N0o0NjGv7jGrRahXJpZkv2LgIeogxaDM4UkhpWND5CClmOhsaswthfFu9Gp3vftmPnsCGIXRCd0NOdCc009WKRh3ml2cJp3CnvRei99vHrwdj5yJWo8ZDpYAFEpQ+g3nikCGc8MMPz67/XgdNGowRu5sKwDpKuZc5PUjPyI2oYXgjmFHoipjbiQzphxoXOsr7QKwufQdt1B6zP6MwYmGp0n2DEIQE5NDVajYhNqom++c+l6Anlte714aniRcSVrVmP5WeFPqUU7Nokp0xuDDa3/+fB+4ajUxsSWuTyvGaGVmZaS+I2QiNuDGIJThSKIGooTkBuYbqECqc21XcIezrnceOtp+FUHqBaBJZ4xbj4pS9RT619QaPxvQXVseVN76nwxeql1RHOSahBljlsgUWxF3zeZKhEdqQ8gAFjyEON91l3JULx4rwilJZmhkwmNy4nfgbGFlIUghwOMbJH3l8Ce2qhAtMK/fszD3TDqLfhnBRIXYCJAMGJACEzvVOFdeWc5b3l123cnfOB74Xh4dZ5z6m0qZSxaoVPQRTo62y0kH8QQBgGn8RbloNbuxrK7irGwp/OcZ5S2kGWKiYXthi+Ef4aCiSmPbpi8n3ypRrU4wJfL/9no6af4vwR4Ejgg1TAAP6BI4FQDYPplrW7xdfh3BHrxe857andoc/ZsK2YHWwhViUUHOkwr4R/8DqQE8PRr5A/Z5cpLvgixxaasm2eTbo3Sig6GO4RjiAiFmIhMjtWVp50Opwaz7L0tzLbX4ea49IUFtRIpHTUxlDseSB1SKl+1Z6BqS3V2d056q3sbexZ253VOa1hnK12rUxpGITzGMT8j8xJjA2D2dOM52GbMJ8CLsHynFZ9TlauOCYpmhPCCuoKchs+J8Y02lbKclabIsgC8UsqW2DvlXvQyBIkQ9R0aLq06QEUeUnJbnmagbhxz2nbjeKJ7U3ueeA519262Z6xfp1X3TGY8FDABIh4UAAW293vnA9wlzNK+1rNMp8OeRZTjkA6KDIXUhfOCl4MWiT+Or5SVngWlCbJQvJ7JFtfy46fzygEJEYggNSrGOBJGWFEMXDhmJ20gcgB2QXxYevN8yHcLdTlxLmn/X39WT0yuPiMyUyRXFosGPfgA6v/aWM8jwHayBKkIoDqXkZHbiY6H2YSygkiG4omYjECTBJvfpuyvJLn6xVPU5+F571UA0w7pGssnUze6Q+5OCFwbYkJtynPueJ17BnzVeot4c3jecbVqFF61WENKBUB6MS4mdxXFCC35v+ps3XTOssKQtZ2qDqB4llWRporPiAGEd4XUh32K94xjkkqaZKRSrfu66cdt1Kvfz/Ci/XsMsRvpKMs3MkVoUDNaOWKoailzrXX2etx6NXspd313zW8makJhoVW4Tb5B7jJZJlcXWwo4+ljr4d5Q0PXDirUrrKihvJgzk5mIEodXg7WCjIMOiG+JsZKwmZuk/6xduLXEJdNb30vtpfpsC8Eb1SmiNI1CQU8HWD1k8mtEceJ2KH0jelR8SHmqeCZxRGiOYS9Y+k83Q543WyaLF1AMov0W7czfqNEqxji6qKsrolSZM5KTjeaGgoWIhUiDa4d/jCKPx5d4o/qribVbxDLQZ+AM7TP7lwmmGC8kcjS2Qj9PnldbYlRqJnEid5B5tnpjfLN64Xdocx9r32NGWdFNIkU/N8corxtzDD38Hu9Y4APVb8YYu/qr0KFsmSmT/YtiiMKGPoajhQeHHosKkHaYtqFKquO2X8Rizfrdkeyk+j8HDBm/Jy40ID/FSa1X8l8cam5vYnXTeJt7G3j4e4V3nHMXbJdkVlkYUJBFJzl/KA8bjQ0j/0vvbOG71XDFZLtgrR+k25orkSKOtIn4hiGDz4NbheiJ6pGolnqgZKgftw7Aic6M3EvoqPlyB2YXQiV3MfA8UEovVjhfYGh9cFF1KXg3fYJ60Xyvdg9ztm63Yipc41H9RMc5miwMHOkNaP4P87zidNddyBS8BrLppeqZuZGyj32IIITvhN+DEYZVirSQppeWoSWnWLRWv4vNitzd6Qz2EAh6FCwj7i59PZxJW1UtYHhoQW7Ldrh3XXuGfAh6uHd6c2xsI2WPXoJSXEczOt8rKB77DxYBOfPa4+3Y5sgLvA+xc6cxnAWV4Y0Nh6iFLIJ7gwWEXIenkOOVy57Yp3a0qb48zjLcHeXg92sFzxSkIUIvTjnHSb1SVV3aZyxu+HXXeDp6n3yXe5F3oXLbbf9lk1zSUw1HJjxhLHgebhBrBHj0ved11tjJpb1Ds0qmy56ulRWP24hmhXGFTISvhT2J/45Cktue+qeksaa9bcul1+/mWPSkAtEPyR6yLjY8ZUkMU8JbyGfmbfNzAnjkfJ95L3w2dy10128jaClfFFNKS446LC+FJCQSqwTX89vo7tcNzBy/4rDrqlagr5WQkBGKCobFg8CGnYXzh1GNE5Z3mlqlRbE6vMHIAtXb49nyZgErEHgfeS3AN8dIfFO2W7Bm022BcnV3nniJeRB8Qne9cm9w/We5X+ZW40ksPYkvuyEHFekGhfbA6gnZWMqnv+KzNanPnnCXrJA9iomG2oZBhE+FJIekjeyUlJuZpWev+7mJySLWPuH372EAIg+FHJwsqzhDQn9R3FsxY5VtW3SRdtN7zXoZeiV543Pjb1FnhGA7VhRKP0ADMUklghW6CNX54OlK2YHPlcBStlypVp/+l3CRI4s8hbuCLYVJg1eIQYuJk2OavqXNsPa5DMcK1TLjNPCNADsPXh14KLc420TdUgxbRGJ1bfFxUne8e2J5TXs5ehx08m3NaJpeEFbuS/RA5DOBJbUaYApr91LsRN+d0G3B9bN8qCWeuJhykZiLU4d8g06Ft4QthqCKtZEUmamiHK2MuKDGndGE4YPvbv1GDasZJSkENyVCUlHqWMljR2u9ct9zw3rjewN6D3nadX5xX2r4YKRYlkymQN40VyggGqcKi/+87HDfZdFQxMC3gampob6ZwZOwi8aHsYRDhICGloezjOuRUZnpoo6st7Y6w+zODeHr7gn7xgxKFmsoWjabQgpRTVlHYlNnbXJLddB7PHuTfL55XnaRcWBogGTwWUVOhkOkMzUoXBfEDDr9re3A4WfQC8ePuLCsOaIInM+SMY6eiUOFFYPDhMyH+okBkgmaJ6E7q5a4hcPLz1Tgle+/+awJ8xkMJ/gzDkFPTExX5GEDafNyo3W/eXV6kHkTeOZ4pXOYa0BiD1mQTspC0zWRKGsbjAvR+wPwqOJT1R3GmbpNryujfpn7ksGLmomshVOEyoNAiHeN8o9YmK6hM6kxtp7BB9F33qPqhfuRCH8WPCR2M98+SE1PVPZfb2zLcIp0iXrNe+B87HpQdlxxHW6iYvtaK0/gRJ42OiwtHkcOQAHk8HXkPtVtxta7YrBWpRidgpZ7jkWIn4I4hdyFzoaYihyQ75eNn6KoBbTmvy7Pgto46Tv5yQg1GKYlhDBwPZlMglRKX9lpNnDmdU14H3owe556u3lIc1xtHGVuXn5QG0ZuOWwsdh0IEPsCk+8I43fVQsvnunOxaKKsngqWL4z/h8yDfoQCgo2FNYnKkDeYAqDcqE2yyb+azILbCOhD948DjRTLIP4wNT7DS8hUs2BqaultKXT+eNV9VX06ehd4k3KZbF9mdlyBT2BIAzmULU0hKBKdAVz1F+XB1uDINbslsvilDZ0WlNiNm4sKhvaEHIU2hpiKX4/SmKCexqRssUu8pMk22uvnoPSLBowRjyBkMEo8OktaUh5fGmZxbpR1tngjeqR9JXoUej91ym0lZsldYVNXSOw7cC6UHsESaQPO8zzm7dfwyz6+MrC7piaeUZVHjy6KE4S+hGmEbYesiPSOXZQ2m3+nUbEFuxPLPNZW5t31TwPBDuYgZC0GPJVHaVPyXRhmfWvJc7l4oXmMfPd5/3YUcwVt32YRXvBWpklGPDUuLyJOFJgFnvWv6QTb181vwK2ySacEoBOVGJBPiR2IR4OUgkSFnYjLjxqUKZ/9pemwtrwqx6XW+uNu9MQA/A+VHm0rzDwUR0pQ6lygZdRs43GheCt6bH2zfeJ5pHYkcP1nJmBXV1FK5j04MdQh2hPHBYv2wOnr3QrNQ8AitF+nM6C9lUyRtIvohi6EiYOUhU2IJI0ilA6bG6WAr3q5QcZr1L3ijPJe/1cNtRwVKwc5TERgUJtaoGZ9bB1xoHe2eJt7BHrxeAF1Ym6yaLZgXVWRTPg+ZTLjIxwW1Qbj+J7oHtxs0DzAyrKOqM+f6JVUkSuLK4f7hZuDtIXSiOyNjJG5mlmjk7AGulLIU9cu45/tBvwdDXsd+yssN5dCMU/MWbRhrW0Wc2N0iHn4fLN7jnfude5woWdwYbJYo0nYQYQ1wCRJF08IIvrs60ffPNLGxBG3R6uZnviYUo8BiveHE4TrgiKE6Igxi8WSnpmuo9mt5bkGxtLSueIs8Gj+oQq9G1AorjZiQ2VNc1lqZMNqEnNidNJ4RX0ie/h3f3kNcm5qGGRTWD9N5j86NE0niReSCxr6wexr35zRNMNptqmpZqDwliWSLY7eh9KE0YPPg8yJoovckIab3aFDrQO3tsXA0H7gcO6++ooLIBj0JWA280BbS7xYmGL5aTBxDHdTeNh6O33CeiR3SW9FaLNjglogTqJB1DI0KX0alAir/Ifv1+GF03TD87i4rJ2gbZcDkriMn4hohe+FGoTehn2M1Y+ZmJahnqpjt7rCPNHd4Jnqx/q+CSUa+SMnMvJAc0zMVkxgg2jGb4tz7XlRfNt7oXjNdAx0q2w/ZYJZuU+WQ7M38ijeG1EMu/568fPir9VXyCK53a6So0aYkpPFi7uKv4PGgiWF9YUKiYqO6ZgZoE+sCrPXwIzRSt166p36agbuFnEjlDKjPZ5MDlZpYZJqhm6idKN5I3z3evN3vHYsdBBtP2YhWzNPSUMFO7As6xzyESr+sPGU4pLVwMfcuaivM6OIm5mTyouhhzeDkYKShTKGGoofkMuYUaBtqPC13b7TzGPcBure+SEI/BVCIlgy2z52ShhXxWAVaEJuhXePd+N6dHuneR94ZnLlbZllIlwwUmtENjqCLKwe8xBTAzfteeU=" type="audio/wav" />
                    Your browser does not support the audio element.
                </audio>
              
</div>

</div>

</div>
</div>

</div>
    </div>
  </div>
</body>

 


</html>