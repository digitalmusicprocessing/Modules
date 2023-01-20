---
layout: module
permalink: /Module2/Video4
title: "CS 372 Module 2: Simple Numpy Tunes Part 4"
excerpt: "CS 372 Module 2: Simple Numpy Tunes Part 4"

info:
  prev: "./Exercise3"
  comments: "true"
---

<p>
Please watch the video below, and be ready to be cold called on Monday to explain what chirps and beats are!
</p>

<iframe width="560" height="315" src="https://www.youtube.com/embed/jwer0GVlxDY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<html>
<head><meta charset="utf-8" />

<title>Part4</title>

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
<h2 id="Chirps-And-Beat-Frequencies">Chirps And Beat Frequencies<a class="anchor-link" href="#Chirps-And-Beat-Frequencies">&#182;</a></h2><p>$y(t) = A \cos(2 \pi f(t) t + \phi)$</p>
<p>Ex) "Linear chirp"
$f(t) = 440 + 440*t$</p>
<p>$y(t) = \cos(2 \pi (440 + 440t)*t)$</p>
<p>$y(t) = \cos(880\pi(t + t^2))$</p>

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
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sr</span> <span class="o">=</span> <span class="mi">44100</span>
<span class="n">t</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">sr</span><span class="p">)</span>
<span class="n">f</span> <span class="o">=</span> <span class="mi">440</span> <span class="o">+</span> <span class="mi">440</span><span class="o">*</span><span class="n">t</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">f</span><span class="o">*</span><span class="n">t</span><span class="p">)</span>
<span class="n">ipd</span><span class="o">.</span><span class="n">Audio</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">rate</span><span class="o">=</span><span class="n">sr</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[2]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">

                <audio  controls="controls" >
                    <source src="data:audio/wav;base64,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" type="audio/wav" />
                    Your browser does not support the audio element.
                </audio>
              
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">f1</span> <span class="o">=</span> <span class="mi">5</span>
<span class="n">f2</span> <span class="o">=</span> <span class="mi">6</span>
<span class="n">t</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">400</span><span class="o">*</span><span class="mi">10</span><span class="p">)</span>
<span class="n">y1</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">f1</span><span class="o">*</span><span class="n">t</span><span class="p">)</span>
<span class="n">y2</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">f2</span><span class="o">*</span><span class="n">t</span><span class="p">)</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">y1</span> <span class="o">+</span> <span class="n">y2</span>
<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">14</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">211</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">y1</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">y2</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">212</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">y</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[3]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x7f007fc42890&gt;]</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">f1</span> <span class="o">=</span> <span class="mi">440</span>
<span class="n">f2</span> <span class="o">=</span> <span class="mi">444</span>
<span class="c1">## Def. Beat frequency: f2 - f1</span>
<span class="n">t</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="n">sr</span><span class="o">*</span><span class="mi">2</span><span class="p">)</span>
<span class="n">y1</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">f1</span><span class="o">*</span><span class="n">t</span><span class="p">)</span>
<span class="n">y2</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">f2</span><span class="o">*</span><span class="n">t</span><span class="p">)</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">y1</span> <span class="o">+</span> <span class="n">y2</span>
<span class="n">ipd</span><span class="o">.</span><span class="n">Audio</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">rate</span><span class="o">=</span><span class="n">sr</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[4]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">

                <audio  controls="controls" >
                    <source src="data:audio/wav;base64,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" type="audio/wav" />
                    Your browser does not support the audio element.
                </audio>
              
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
    </div>
  </div>