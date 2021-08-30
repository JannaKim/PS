import sys

# 좌표들 정렬하고, 기준 하나 잡고 오른쪽으로 탐색하기

n, k = map(int, input().split())

COLOR = [ [] for _ in range(k + 1)]
for _ in range(n):
    y, x, color = map(int, input().split())
    COLOR[color].append((y, x))

ans = 1e9

    # a b
    # c d

def rec(cur, A, B, C, D):
    global k, ans
    if cur == k + 1:
        # print(A, B, C, D, sep = '\n')
        area = abs(C[0] - A[0]) * abs(B[1] - A[1])
        # print(area)
        ans = min(ans, area)
        return

    if cur == 1:
        for y, x in COLOR[cur]:
            a = [y, x]
            b = [y, x]
            c = [y, x]
            d = [y, x]
            rec(cur + 1, a, b, c, d)
    else:
        for y, x in COLOR[cur]:
            a = [ min(A[0], y), min(A[1], x)  ]
            b = [ min(B[0], y), max(B[1], x)  ]
            c = [ max(C[0], y), min(C[1], x)  ]
            d = [ max(D[0], y), max(D[1], x)  ]
            rec(cur + 1, a, b, c, d)




rec(1, -1, -1, -1, -1)
print(ans)


'''
<html lang="ko"><!--begin::Head--><head><style type="text/css">.swal-icon--error{border-color:#f27474;-webkit-animation:animateErrorIcon .5s;animation:animateErrorIcon .5s}.swal-icon--error__x-mark{position:relative;display:block;-webkit-animation:animateXMark .5s;animation:animateXMark .5s}.swal-icon--error__line{position:absolute;height:5px;width:47px;background-color:#f27474;display:block;top:37px;border-radius:2px}.swal-icon--error__line--left{-webkit-transform:rotate(45deg);transform:rotate(45deg);left:17px}.swal-icon--error__line--right{-webkit-transform:rotate(-45deg);transform:rotate(-45deg);right:16px}@-webkit-keyframes animateErrorIcon{0%{-webkit-transform:rotateX(100deg);transform:rotateX(100deg);opacity:0}to{-webkit-transform:rotateX(0deg);transform:rotateX(0deg);opacity:1}}@keyframes animateErrorIcon{0%{-webkit-transform:rotateX(100deg);transform:rotateX(100deg);opacity:0}to{-webkit-transform:rotateX(0deg);transform:rotateX(0deg);opacity:1}}@-webkit-keyframes animateXMark{0%{-webkit-transform:scale(.4);transform:scale(.4);margin-top:26px;opacity:0}50%{-webkit-transform:scale(.4);transform:scale(.4);margin-top:26px;opacity:0}80%{-webkit-transform:scale(1.15);transform:scale(1.15);margin-top:-6px}to{-webkit-transform:scale(1);transform:scale(1);margin-top:0;opacity:1}}@keyframes animateXMark{0%{-webkit-transform:scale(.4);transform:scale(.4);margin-top:26px;opacity:0}50%{-webkit-transform:scale(.4);transform:scale(.4);margin-top:26px;opacity:0}80%{-webkit-transform:scale(1.15);transform:scale(1.15);margin-top:-6px}to{-webkit-transform:scale(1);transform:scale(1);margin-top:0;opacity:1}}.swal-icon--warning{border-color:#f8bb86;-webkit-animation:pulseWarning .75s infinite alternate;animation:pulseWarning .75s infinite alternate}.swal-icon--warning__body{width:5px;height:47px;top:10px;border-radius:2px;margin-left:-2px}.swal-icon--warning__body,.swal-icon--warning__dot{position:absolute;left:50%;background-color:#f8bb86}.swal-icon--warning__dot{width:7px;height:7px;border-radius:50%;margin-left:-4px;bottom:-11px}@-webkit-keyframes pulseWarning{0%{border-color:#f8d486}to{border-color:#f8bb86}}@keyframes pulseWarning{0%{border-color:#f8d486}to{border-color:#f8bb86}}.swal-icon--success{border-color:#a5dc86}.swal-icon--success:after,.swal-icon--success:before{content:"";border-radius:50%;position:absolute;width:60px;height:120px;background:#fff;-webkit-transform:rotate(45deg);transform:rotate(45deg)}.swal-icon--success:before{border-radius:120px 0 0 120px;top:-7px;left:-33px;-webkit-transform:rotate(-45deg);transform:rotate(-45deg);-webkit-transform-origin:60px 60px;transform-origin:60px 60px}.swal-icon--success:after{border-radius:0 120px 120px 0;top:-11px;left:30px;-webkit-transform:rotate(-45deg);transform:rotate(-45deg);-webkit-transform-origin:0 60px;transform-origin:0 60px;-webkit-animation:rotatePlaceholder 4.25s ease-in;animation:rotatePlaceholder 4.25s ease-in}.swal-icon--success__ring{width:80px;height:80px;border:4px solid hsla(98,55%,69%,.2);border-radius:50%;box-sizing:content-box;position:absolute;left:-4px;top:-4px;z-index:2}.swal-icon--success__hide-corners{width:5px;height:90px;background-color:#fff;padding:1px;position:absolute;left:28px;top:8px;z-index:1;-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}.swal-icon--success__line{height:5px;background-color:#a5dc86;display:block;border-radius:2px;position:absolute;z-index:2}.swal-icon--success__line--tip{width:25px;left:14px;top:46px;-webkit-transform:rotate(45deg);transform:rotate(45deg);-webkit-animation:animateSuccessTip .75s;animation:animateSuccessTip .75s}.swal-icon--success__line--long{width:47px;right:8px;top:38px;-webkit-transform:rotate(-45deg);transform:rotate(-45deg);-webkit-animation:animateSuccessLong .75s;animation:animateSuccessLong .75s}@-webkit-keyframes rotatePlaceholder{0%{-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}5%{-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}12%{-webkit-transform:rotate(-405deg);transform:rotate(-405deg)}to{-webkit-transform:rotate(-405deg);transform:rotate(-405deg)}}@keyframes rotatePlaceholder{0%{-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}5%{-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}12%{-webkit-transform:rotate(-405deg);transform:rotate(-405deg)}to{-webkit-transform:rotate(-405deg);transform:rotate(-405deg)}}@-webkit-keyframes animateSuccessTip{0%{width:0;left:1px;top:19px}54%{width:0;left:1px;top:19px}70%{width:50px;left:-8px;top:37px}84%{width:17px;left:21px;top:48px}to{width:25px;left:14px;top:45px}}@keyframes animateSuccessTip{0%{width:0;left:1px;top:19px}54%{width:0;left:1px;top:19px}70%{width:50px;left:-8px;top:37px}84%{width:17px;left:21px;top:48px}to{width:25px;left:14px;top:45px}}@-webkit-keyframes animateSuccessLong{0%{width:0;right:46px;top:54px}65%{width:0;right:46px;top:54px}84%{width:55px;right:0;top:35px}to{width:47px;right:8px;top:38px}}@keyframes animateSuccessLong{0%{width:0;right:46px;top:54px}65%{width:0;right:46px;top:54px}84%{width:55px;right:0;top:35px}to{width:47px;right:8px;top:38px}}.swal-icon--info{border-color:#c9dae1}.swal-icon--info:before{width:5px;height:29px;bottom:17px;border-radius:2px;margin-left:-2px}.swal-icon--info:after,.swal-icon--info:before{content:"";position:absolute;left:50%;background-color:#c9dae1}.swal-icon--info:after{width:7px;height:7px;border-radius:50%;margin-left:-3px;top:19px}.swal-icon{width:80px;height:80px;border-width:4px;border-style:solid;border-radius:50%;padding:0;position:relative;box-sizing:content-box;margin:20px auto}.swal-icon:first-child{margin-top:32px}.swal-icon--custom{width:auto;height:auto;max-width:100%;border:none;border-radius:0}.swal-icon img{max-width:100%;max-height:100%}.swal-title{color:rgba(0,0,0,.65);font-weight:600;text-transform:none;position:relative;display:block;padding:13px 16px;font-size:27px;line-height:normal;text-align:center;margin-bottom:0}.swal-title:first-child{margin-top:26px}.swal-title:not(:first-child){padding-bottom:0}.swal-title:not(:last-child){margin-bottom:13px}.swal-text{font-size:16px;position:relative;float:none;line-height:normal;vertical-align:top;text-align:left;display:inline-block;margin:0;padding:0 10px;font-weight:400;color:rgba(0,0,0,.64);max-width:calc(100% - 20px);overflow-wrap:break-word;box-sizing:border-box}.swal-text:first-child{margin-top:45px}.swal-text:last-child{margin-bottom:45px}.swal-footer{text-align:right;padding-top:13px;margin-top:13px;padding:13px 16px;border-radius:inherit;border-top-left-radius:0;border-top-right-radius:0}.swal-button-container{margin:5px;display:inline-block;position:relative}.swal-button{background-color:#7cd1f9;color:#fff;border:none;box-shadow:none;border-radius:5px;font-weight:600;font-size:14px;padding:10px 24px;margin:0;cursor:pointer}.swal-button:not([disabled]):hover{background-color:#78cbf2}.swal-button:active{background-color:#70bce0}.swal-button:focus{outline:none;box-shadow:0 0 0 1px #fff,0 0 0 3px rgba(43,114,165,.29)}.swal-button[disabled]{opacity:.5;cursor:default}.swal-button::-moz-focus-inner{border:0}.swal-button--cancel{color:#555;background-color:#efefef}.swal-button--cancel:not([disabled]):hover{background-color:#e8e8e8}.swal-button--cancel:active{background-color:#d7d7d7}.swal-button--cancel:focus{box-shadow:0 0 0 1px #fff,0 0 0 3px rgba(116,136,150,.29)}.swal-button--danger{background-color:#e64942}.swal-button--danger:not([disabled]):hover{background-color:#df4740}.swal-button--danger:active{background-color:#cf423b}.swal-button--danger:focus{box-shadow:0 0 0 1px #fff,0 0 0 3px rgba(165,43,43,.29)}.swal-content{padding:0 20px;margin-top:20px;font-size:medium}.swal-content:last-child{margin-bottom:20px}.swal-content__input,.swal-content__textarea{-webkit-appearance:none;background-color:#fff;border:none;font-size:14px;display:block;box-sizing:border-box;width:100%;border:1px solid rgba(0,0,0,.14);padding:10px 13px;border-radius:2px;transition:border-color .2s}.swal-content__input:focus,.swal-content__textarea:focus{outline:none;border-color:#6db8ff}.swal-content__textarea{resize:vertical}.swal-button--loading{color:transparent}.swal-button--loading~.swal-button__loader{opacity:1}.swal-button__loader{position:absolute;height:auto;width:43px;z-index:2;left:50%;top:50%;-webkit-transform:translateX(-50%) translateY(-50%);transform:translateX(-50%) translateY(-50%);text-align:center;pointer-events:none;opacity:0}.swal-button__loader div{display:inline-block;float:none;vertical-align:baseline;width:9px;height:9px;padding:0;border:none;margin:2px;opacity:.4;border-radius:7px;background-color:hsla(0,0%,100%,.9);transition:background .2s;-webkit-animation:swal-loading-anim 1s infinite;animation:swal-loading-anim 1s infinite}.swal-button__loader div:nth-child(3n+2){-webkit-animation-delay:.15s;animation-delay:.15s}.swal-button__loader div:nth-child(3n+3){-webkit-animation-delay:.3s;animation-delay:.3s}@-webkit-keyframes swal-loading-anim{0%{opacity:.4}20%{opacity:.4}50%{opacity:1}to{opacity:.4}}@keyframes swal-loading-anim{0%{opacity:.4}20%{opacity:.4}50%{opacity:1}to{opacity:.4}}.swal-overlay{position:fixed;top:0;bottom:0;left:0;right:0;text-align:center;font-size:0;overflow-y:auto;background-color:rgba(0,0,0,.4);z-index:10000;pointer-events:none;opacity:0;transition:opacity .3s}.swal-overlay:before{content:" ";display:inline-block;vertical-align:middle;height:100%}.swal-overlay--show-modal{opacity:1;pointer-events:auto}.swal-overlay--show-modal .swal-modal{opacity:1;pointer-events:auto;box-sizing:border-box;-webkit-animation:showSweetAlert .3s;animation:showSweetAlert .3s;will-change:transform}.swal-modal{width:478px;opacity:0;pointer-events:none;background-color:#fff;text-align:center;border-radius:5px;position:static;margin:20px auto;display:inline-block;vertical-align:middle;-webkit-transform:scale(1);transform:scale(1);-webkit-transform-origin:50% 50%;transform-origin:50% 50%;z-index:10001;transition:opacity .2s,-webkit-transform .3s;transition:transform .3s,opacity .2s;transition:transform .3s,opacity .2s,-webkit-transform .3s}@media (max-width:500px){.swal-modal{width:calc(100% - 20px)}}@-webkit-keyframes showSweetAlert{0%{-webkit-transform:scale(1);transform:scale(1)}1%{-webkit-transform:scale(.5);transform:scale(.5)}45%{-webkit-transform:scale(1.05);transform:scale(1.05)}80%{-webkit-transform:scale(.95);transform:scale(.95)}to{-webkit-transform:scale(1);transform:scale(1)}}@keyframes showSweetAlert{0%{-webkit-transform:scale(1);transform:scale(1)}1%{-webkit-transform:scale(.5);transform:scale(.5)}45%{-webkit-transform:scale(1.05);transform:scale(1.05)}80%{-webkit-transform:scale(.95);transform:scale(.95)}to{-webkit-transform:scale(1);transform:scale(1)}}</style><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="vs/editor/editor.main" src="/js/monaco-editor/min/vs/editor/editor.main.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="vs/editor/editor.main.nls" src="/js/monaco-editor/min/vs/editor/editor.main.nls.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="vs/basic-languages/python/python" src="/js/monaco-editor/min/vs/basic-languages/python/python.js"></script><base href="">
        <meta charset="utf-8">
        <title>Code Editor : SOFTEER</title>
        <meta name="description" content="Updates and statistics">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <!--begin::Page Vendors Styles(used by this page)-->
        <!--end::Page Vendors Styles-->
        <!--begin::Global Theme Styles(used by all pages)-->
        <link href="/assets/plugins/global/plugins.bundle.css" rel="stylesheet" type="text/css">
        <link href="/assets/plugins/custom/prismjs/prismjs.bundle.css" rel="stylesheet" type="text/css">
        <link href="/assets/css/style.bundle.css" rel="stylesheet" type="text/css">
        <!--end::Global Theme Styles-->
        
        <!-- 프리랜서 css -->
        <link rel="stylesheet" type="text/css" href="/common/css/common.css">
        <link rel="stylesheet" type="text/css" href="/common/css/common_new.css">
        
        <!-- Notification css -->
        <link href="/assets/css/simple-notify.min.css" rel="stylesheet">
        <link href="/assets/css/OverlayScrollbars.min.css" rel="stylesheet">
        
        <link href="/assets/css/style.scroll_light.css" id="SfScroll" rel="stylesheet">
        <link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="/js/monaco-editor/min/vs/editor/editor.main.css"><link rel="stylesheet" href="//cdn.jsdelivr.net/npm/hack-font@3.3.0/build/web/hack-subset.css">
        <style type="text/css">
            #submitCn::after {
                left: 73%;
            }
            
            .type-docs::after {
                left: initial;
            }
            body, * {
                font-family : unset;
            }
        </style>
        
        <!-- Jquery -->
        <script type="text/javascript" async="" src="https://cdn.channel.io/plugin/ch-plugin-web.js" charset="UTF-8"></script><script src="/common/js/jquery.js"></script>
        <script>
            var testType = "certification";
            window.addEventListener('beforeunload', (event) => {
                console.log(monaco_editor_obj.getValue());
                if(testType == "certification" || testType == "HMG") {
                    var code = monaco_editor_obj.getValue();
                    var save = document.getElementsByClassName('btn_save');
                    console.log(save);
                    var ajax_data = {
                        eventIdx: save[0].dataset.eventidx,
                        psProblemId: save[0].dataset.psproblemid,
                        language: save[0].dataset.language,
                        groupId: save[0].dataset.groupid,
                        practiceId: save[0].dataset.practiceid,
                        languageSn: save[0].dataset.languagesn,
                        eventType : save[0].dataset.eventtype,
                        _csrf: jQuery("#_csrf").val(),
                        code : code,
                        ajax : "true"
                    };
                    console.log(ajax_data);
                    jQuery.ajax({
                        type: 'post',
                        url: '/practiceSubmissions/saveCodeEditor.do',
                        data: ajax_data,
                        //dataType: "json",
                        success: function(data) {
                            console.log("자동저장");
                        }
                    });
                }
            });
            /* 
            $(window).on('beforeunload', function(e){
                if(testType == "Certification" || testType == "HMG") {
                    // 사용자에 의해 화면 종료
                    alert("사용자가 창 닫음.");
                    var data = {
                        idx: $('#data-eventIdx').val(),
                        psProblemId: $('#data-psProblemId').val(),
                        _csrf: $('#_csrf').val()
                    };
                    // opener.parent.location.reload(); 
                    $.ajax({
                        url: "/practiceSubmissions/closeEditor.do",
                        type: "POST",
                        data: data,
                        dataType: "json",
                        success:function(data) {
                        }
                     });
                }
                else{
                }
            }); 
            */
            
        </script>
    <style type="text/css">.apexcharts-canvas {
  position: relative;
  user-select: none;
  /* cannot give overflow: hidden as it will crop tooltips which overflow outside chart area */
}


/* scrollbar is not visible by default for legend, hence forcing the visibility */
.apexcharts-canvas ::-webkit-scrollbar {
  -webkit-appearance: none;
  width: 6px;
}

.apexcharts-canvas ::-webkit-scrollbar-thumb {
  border-radius: 4px;
  background-color: rgba(0, 0, 0, .5);
  box-shadow: 0 0 1px rgba(255, 255, 255, .5);
  -webkit-box-shadow: 0 0 1px rgba(255, 255, 255, .5);
}

.apexcharts-canvas.apexcharts-theme-dark {
  background: #424242;
}

.apexcharts-inner {
  position: relative;
}

.apexcharts-text tspan {
  font-family: inherit;
}

.legend-mouseover-inactive {
  transition: 0.15s ease all;
  opacity: 0.20;
}

.apexcharts-series-collapsed {
  opacity: 0;
}

.apexcharts-tooltip {
  border-radius: 5px;
  box-shadow: 2px 2px 6px -4px #999;
  cursor: default;
  font-size: 14px;
  left: 62px;
  opacity: 0;
  pointer-events: none;
  position: absolute;
  top: 20px;
  overflow: hidden;
  white-space: nowrap;
  z-index: 12;
  transition: 0.15s ease all;
}

.apexcharts-tooltip.apexcharts-active {
  opacity: 1;
  transition: 0.15s ease all;
}

.apexcharts-tooltip.apexcharts-theme-light {
  border: 1px solid #e3e3e3;
  background: rgba(255, 255, 255, 0.96);
}

.apexcharts-tooltip.apexcharts-theme-dark {
  color: #fff;
  background: rgba(30, 30, 30, 0.8);
}

.apexcharts-tooltip * {
  font-family: inherit;
}


.apexcharts-tooltip-title {
  padding: 6px;
  font-size: 15px;
  margin-bottom: 4px;
}

.apexcharts-tooltip.apexcharts-theme-light .apexcharts-tooltip-title {
  background: #ECEFF1;
  border-bottom: 1px solid #ddd;
}

.apexcharts-tooltip.apexcharts-theme-dark .apexcharts-tooltip-title {
  background: rgba(0, 0, 0, 0.7);
  border-bottom: 1px solid #333;
}

.apexcharts-tooltip-text-value,
.apexcharts-tooltip-text-z-value {
  display: inline-block;
  font-weight: 600;
  margin-left: 5px;
}

.apexcharts-tooltip-text-z-label:empty,
.apexcharts-tooltip-text-z-value:empty {
  display: none;
}

.apexcharts-tooltip-text-value,
.apexcharts-tooltip-text-z-value {
  font-weight: 600;
}

.apexcharts-tooltip-marker {
  width: 12px;
  height: 12px;
  position: relative;
  top: 0px;
  margin-right: 10px;
  border-radius: 50%;
}

.apexcharts-tooltip-series-group {
  padding: 0 10px;
  display: none;
  text-align: left;
  justify-content: left;
  align-items: center;
}

.apexcharts-tooltip-series-group.apexcharts-active .apexcharts-tooltip-marker {
  opacity: 1;
}

.apexcharts-tooltip-series-group.apexcharts-active,
.apexcharts-tooltip-series-group:last-child {
  padding-bottom: 4px;
}

.apexcharts-tooltip-series-group-hidden {
  opacity: 0;
  height: 0;
  line-height: 0;
  padding: 0 !important;
}

.apexcharts-tooltip-y-group {
  padding: 6px 0 5px;
}

.apexcharts-tooltip-candlestick {
  padding: 4px 8px;
}

.apexcharts-tooltip-candlestick>div {
  margin: 4px 0;
}

.apexcharts-tooltip-candlestick span.value {
  font-weight: bold;
}

.apexcharts-tooltip-rangebar {
  padding: 5px 8px;
}

.apexcharts-tooltip-rangebar .category {
  font-weight: 600;
  color: #777;
}

.apexcharts-tooltip-rangebar .series-name {
  font-weight: bold;
  display: block;
  margin-bottom: 5px;
}

.apexcharts-xaxistooltip {
  opacity: 0;
  padding: 9px 10px;
  pointer-events: none;
  color: #373d3f;
  font-size: 13px;
  text-align: center;
  border-radius: 2px;
  position: absolute;
  z-index: 10;
  background: #ECEFF1;
  border: 1px solid #90A4AE;
  transition: 0.15s ease all;
}

.apexcharts-xaxistooltip.apexcharts-theme-dark {
  background: rgba(0, 0, 0, 0.7);
  border: 1px solid rgba(0, 0, 0, 0.5);
  color: #fff;
}

.apexcharts-xaxistooltip:after,
.apexcharts-xaxistooltip:before {
  left: 50%;
  border: solid transparent;
  content: " ";
  height: 0;
  width: 0;
  position: absolute;
  pointer-events: none;
}

.apexcharts-xaxistooltip:after {
  border-color: rgba(236, 239, 241, 0);
  border-width: 6px;
  margin-left: -6px;
}

.apexcharts-xaxistooltip:before {
  border-color: rgba(144, 164, 174, 0);
  border-width: 7px;
  margin-left: -7px;
}

.apexcharts-xaxistooltip-bottom:after,
.apexcharts-xaxistooltip-bottom:before {
  bottom: 100%;
}

.apexcharts-xaxistooltip-top:after,
.apexcharts-xaxistooltip-top:before {
  top: 100%;
}

.apexcharts-xaxistooltip-bottom:after {
  border-bottom-color: #ECEFF1;
}

.apexcharts-xaxistooltip-bottom:before {
  border-bottom-color: #90A4AE;
}

.apexcharts-xaxistooltip-bottom.apexcharts-theme-dark:after {
  border-bottom-color: rgba(0, 0, 0, 0.5);
}

.apexcharts-xaxistooltip-bottom.apexcharts-theme-dark:before {
  border-bottom-color: rgba(0, 0, 0, 0.5);
}

.apexcharts-xaxistooltip-top:after {
  border-top-color: #ECEFF1
}

.apexcharts-xaxistooltip-top:before {
  border-top-color: #90A4AE;
}

.apexcharts-xaxistooltip-top.apexcharts-theme-dark:after {
  border-top-color: rgba(0, 0, 0, 0.5);
}

.apexcharts-xaxistooltip-top.apexcharts-theme-dark:before {
  border-top-color: rgba(0, 0, 0, 0.5);
}

.apexcharts-xaxistooltip.apexcharts-active {
  opacity: 1;
  transition: 0.15s ease all;
}

.apexcharts-yaxistooltip {
  opacity: 0;
  padding: 4px 10px;
  pointer-events: none;
  color: #373d3f;
  font-size: 13px;
  text-align: center;
  border-radius: 2px;
  position: absolute;
  z-index: 10;
  background: #ECEFF1;
  border: 1px solid #90A4AE;
}

.apexcharts-yaxistooltip.apexcharts-theme-dark {
  background: rgba(0, 0, 0, 0.7);
  border: 1px solid rgba(0, 0, 0, 0.5);
  color: #fff;
}

.apexcharts-yaxistooltip:after,
.apexcharts-yaxistooltip:before {
  top: 50%;
  border: solid transparent;
  content: " ";
  height: 0;
  width: 0;
  position: absolute;
  pointer-events: none;
}

.apexcharts-yaxistooltip:after {
  border-color: rgba(236, 239, 241, 0);
  border-width: 6px;
  margin-top: -6px;
}

.apexcharts-yaxistooltip:before {
  border-color: rgba(144, 164, 174, 0);
  border-width: 7px;
  margin-top: -7px;
}

.apexcharts-yaxistooltip-left:after,
.apexcharts-yaxistooltip-left:before {
  left: 100%;
}

.apexcharts-yaxistooltip-right:after,
.apexcharts-yaxistooltip-right:before {
  right: 100%;
}

.apexcharts-yaxistooltip-left:after {
  border-left-color: #ECEFF1;
}

.apexcharts-yaxistooltip-left:before {
  border-left-color: #90A4AE;
}

.apexcharts-yaxistooltip-left.apexcharts-theme-dark:after {
  border-left-color: rgba(0, 0, 0, 0.5);
}

.apexcharts-yaxistooltip-left.apexcharts-theme-dark:before {
  border-left-color: rgba(0, 0, 0, 0.5);
}

.apexcharts-yaxistooltip-right:after {
  border-right-color: #ECEFF1;
}

.apexcharts-yaxistooltip-right:before {
  border-right-color: #90A4AE;
}

.apexcharts-yaxistooltip-right.apexcharts-theme-dark:after {
  border-right-color: rgba(0, 0, 0, 0.5);
}

.apexcharts-yaxistooltip-right.apexcharts-theme-dark:before {
  border-right-color: rgba(0, 0, 0, 0.5);
}

.apexcharts-yaxistooltip.apexcharts-active {
  opacity: 1;
}

.apexcharts-yaxistooltip-hidden {
  display: none;
}

.apexcharts-xcrosshairs,
.apexcharts-ycrosshairs {
  pointer-events: none;
  opacity: 0;
  transition: 0.15s ease all;
}

.apexcharts-xcrosshairs.apexcharts-active,
.apexcharts-ycrosshairs.apexcharts-active {
  opacity: 1;
  transition: 0.15s ease all;
}

.apexcharts-ycrosshairs-hidden {
  opacity: 0;
}

.apexcharts-selection-rect {
  cursor: move;
}

.svg_select_boundingRect, .svg_select_points_rot {
  pointer-events: none;
  opacity: 0;
  visibility: hidden;
}
.apexcharts-selection-rect + g .svg_select_boundingRect,
.apexcharts-selection-rect + g .svg_select_points_rot {
  opacity: 0;
  visibility: hidden;
}

.apexcharts-selection-rect + g .svg_select_points_l,
.apexcharts-selection-rect + g .svg_select_points_r {
  cursor: ew-resize;
  opacity: 1;
  visibility: visible;
}

.svg_select_points {
  fill: #efefef;
  stroke: #333;
  rx: 2;
}

.apexcharts-canvas.apexcharts-zoomable .hovering-zoom {
  cursor: crosshair
}

.apexcharts-canvas.apexcharts-zoomable .hovering-pan {
  cursor: move
}

.apexcharts-zoom-icon,
.apexcharts-zoomin-icon,
.apexcharts-zoomout-icon,
.apexcharts-reset-icon,
.apexcharts-pan-icon,
.apexcharts-selection-icon,
.apexcharts-menu-icon,
.apexcharts-toolbar-custom-icon {
  cursor: pointer;
  width: 20px;
  height: 20px;
  line-height: 24px;
  color: #6E8192;
  text-align: center;
}

.apexcharts-zoom-icon svg,
.apexcharts-zoomin-icon svg,
.apexcharts-zoomout-icon svg,
.apexcharts-reset-icon svg,
.apexcharts-menu-icon svg {
  fill: #6E8192;
}

.apexcharts-selection-icon svg {
  fill: #444;
  transform: scale(0.76)
}

.apexcharts-theme-dark .apexcharts-zoom-icon svg,
.apexcharts-theme-dark .apexcharts-zoomin-icon svg,
.apexcharts-theme-dark .apexcharts-zoomout-icon svg,
.apexcharts-theme-dark .apexcharts-reset-icon svg,
.apexcharts-theme-dark .apexcharts-pan-icon svg,
.apexcharts-theme-dark .apexcharts-selection-icon svg,
.apexcharts-theme-dark .apexcharts-menu-icon svg,
.apexcharts-theme-dark .apexcharts-toolbar-custom-icon svg {
  fill: #f3f4f5;
}

.apexcharts-canvas .apexcharts-zoom-icon.apexcharts-selected svg,
.apexcharts-canvas .apexcharts-selection-icon.apexcharts-selected svg,
.apexcharts-canvas .apexcharts-reset-zoom-icon.apexcharts-selected svg {
  fill: #008FFB;
}

.apexcharts-theme-light .apexcharts-selection-icon:not(.apexcharts-selected):hover svg,
.apexcharts-theme-light .apexcharts-zoom-icon:not(.apexcharts-selected):hover svg,
.apexcharts-theme-light .apexcharts-zoomin-icon:hover svg,
.apexcharts-theme-light .apexcharts-zoomout-icon:hover svg,
.apexcharts-theme-light .apexcharts-reset-icon:hover svg,
.apexcharts-theme-light .apexcharts-menu-icon:hover svg {
  fill: #333;
}

.apexcharts-selection-icon,
.apexcharts-menu-icon {
  position: relative;
}

.apexcharts-reset-icon {
  margin-left: 5px;
}

.apexcharts-zoom-icon,
.apexcharts-reset-icon,
.apexcharts-menu-icon {
  transform: scale(0.85);
}

.apexcharts-zoomin-icon,
.apexcharts-zoomout-icon {
  transform: scale(0.7)
}

.apexcharts-zoomout-icon {
  margin-right: 3px;
}

.apexcharts-pan-icon {
  transform: scale(0.62);
  position: relative;
  left: 1px;
  top: 0px;
}

.apexcharts-pan-icon svg {
  fill: #fff;
  stroke: #6E8192;
  stroke-width: 2;
}

.apexcharts-pan-icon.apexcharts-selected svg {
  stroke: #008FFB;
}

.apexcharts-pan-icon:not(.apexcharts-selected):hover svg {
  stroke: #333;
}

.apexcharts-toolbar {
  position: absolute;
  z-index: 11;
  max-width: 176px;
  text-align: right;
  border-radius: 3px;
  padding: 0px 6px 2px 6px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.apexcharts-menu {
  background: #fff;
  position: absolute;
  top: 100%;
  border: 1px solid #ddd;
  border-radius: 3px;
  padding: 3px;
  right: 10px;
  opacity: 0;
  min-width: 110px;
  transition: 0.15s ease all;
  pointer-events: none;
}

.apexcharts-menu.apexcharts-menu-open {
  opacity: 1;
  pointer-events: all;
  transition: 0.15s ease all;
}

.apexcharts-menu-item {
  padding: 6px 7px;
  font-size: 12px;
  cursor: pointer;
}

.apexcharts-theme-light .apexcharts-menu-item:hover {
  background: #eee;
}

.apexcharts-theme-dark .apexcharts-menu {
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
}

@media screen and (min-width: 768px) {
  .apexcharts-canvas:hover .apexcharts-toolbar {
    opacity: 1;
  }
}

.apexcharts-datalabel.apexcharts-element-hidden {
  opacity: 0;
}

.apexcharts-pie-label,
.apexcharts-datalabels,
.apexcharts-datalabel,
.apexcharts-datalabel-label,
.apexcharts-datalabel-value {
  cursor: default;
  pointer-events: none;
}

.apexcharts-pie-label-delay {
  opacity: 0;
  animation-name: opaque;
  animation-duration: 0.3s;
  animation-fill-mode: forwards;
  animation-timing-function: ease;
}

.apexcharts-canvas .apexcharts-element-hidden {
  opacity: 0;
}

.apexcharts-hide .apexcharts-series-points {
  opacity: 0;
}

.apexcharts-gridline,
.apexcharts-annotation-rect,
.apexcharts-tooltip .apexcharts-marker,
.apexcharts-area-series .apexcharts-area,
.apexcharts-line,
.apexcharts-zoom-rect,
.apexcharts-toolbar svg,
.apexcharts-area-series .apexcharts-series-markers .apexcharts-marker.no-pointer-events,
.apexcharts-line-series .apexcharts-series-markers .apexcharts-marker.no-pointer-events,
.apexcharts-radar-series path,
.apexcharts-radar-series polygon {
  pointer-events: none;
}


/* markers */

.apexcharts-marker {
  transition: 0.15s ease all;
}

@keyframes opaque {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}


/* Resize generated styles */

@keyframes resizeanim {
  from {
    opacity: 0;
  }
  to {
    opacity: 0;
  }
}

.resize-triggers {
  animation: 1ms resizeanim;
  visibility: hidden;
  opacity: 0;
}

.resize-triggers,
.resize-triggers>div,
.contract-trigger:before {
  content: " ";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  overflow: hidden;
}

.resize-triggers>div {
  background: #eee;
  overflow: auto;
}

.contract-trigger:before {
  width: 200%;
  height: 200%;
}</style><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 5px 0px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 5px; -webkit-border-radius: 5px; -moz-border-radius: 5px; -khtml-border-radius: 5px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 1px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: .7em}
.MathJax_MenuRadioCheck.RTL {right: .7em; left: auto}
.MathJax_MenuLabel {padding: 1px 2em 3px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #DDDDDD; margin: 4px 3px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: #606872; color: white}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MathJax_Preview .MJXf-math {color: inherit!important}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css" media="screen" class="monaco-colors">.monaco-editor, .monaco-editor-background, .monaco-editor .inputarea.ime-input { background-color: #fffffe; }
.monaco-editor, .monaco-editor .inputarea.ime-input { color: #000000; }
.monaco-editor .margin { background-color: #fffffe; }
.monaco-editor .rangeHighlight { background-color: rgba(253, 255, 0, 0.2); }
.monaco-editor .symbolHighlight { background-color: rgba(234, 92, 0, 0.33); }
.vs-whitespace { color: rgba(51, 51, 51, 0.2) !important; }
.monaco-editor .line-numbers { color: #237893; }
.monaco-editor .current-line ~ .line-numbers { color: #0b216f; }
.monaco-editor .view-overlays .current-line { border: 2px solid #eeeeee; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #eeeeee; }
.monaco-editor .lines-content .cigr { box-shadow: 1px 0 0 0 #d3d3d3 inset; }
.monaco-editor .lines-content .cigra { box-shadow: 1px 0 0 0 #939393 inset; }
.monaco-editor .view-ruler { box-shadow: 1px 0 0 0 #d3d3d3 inset; }
.monaco-editor .cursor { background-color: #000000; border-color: #000000; color: #ffffff; }
.monaco-editor .minimap-slider, .monaco-editor .minimap-slider .minimap-slider-horizontal { background: rgba(100, 100, 100, 0.2); }
.monaco-editor .minimap-slider:hover, .monaco-editor .minimap-slider:hover .minimap-slider-horizontal { background: rgba(100, 100, 100, 0.35); }
.monaco-editor .minimap-slider.active, .monaco-editor .minimap-slider.active .minimap-slider-horizontal { background: rgba(0, 0, 0, 0.3); }
.monaco-editor .minimap-shadow-visible { box-shadow: #dddddd -6px 0 6px -6px inset; }
.monaco-editor .scroll-decoration { box-shadow: #dddddd 0 6px 6px -6px inset; }
.monaco-editor .focused .selected-text { background-color: #add6ff; }
.monaco-editor .selected-text { background-color: #e5ebf1; }
.monaco-editor .codelens-decoration { color: #999999; }
.monaco-editor .codelens-decoration .codicon { color: #999999; }
.monaco-editor .codelens-decoration > a:hover { color: #0000ff !important; }
.monaco-editor .codelens-decoration > a:hover .codicon { color: #0000ff !important; }

			.monaco-editor .zone-widget .codicon-error,
			.markers-panel .marker-icon.codicon-error,
			.extensions-viewlet > .extensions .codicon-error,
			.monaco-dialog-box .dialog-message-row .codicon-error {
				color: #e51400;
			}
		

			.monaco-editor .zone-widget .codicon-warning,
			.markers-panel .marker-icon.codicon-warning,
			.extensions-viewlet > .extensions .codicon-warning,
			.extension-editor .codicon-warning,
			.monaco-dialog-box .dialog-message-row .codicon-warning {
				color: #e9a700;
			}
		

			.monaco-editor .zone-widget .codicon-info,
			.markers-panel .marker-icon.codicon-info,
			.extensions-viewlet > .extensions .codicon-info,
			.extension-editor .codicon-info,
			.monaco-dialog-box .dialog-message-row .codicon-info {
				color: #75beff;
			}
		
.monaco-editor .tokens-inspect-widget { border: 1px solid #c8c8c8; }
.monaco-editor .tokens-inspect-widget .tokens-inspect-separator { background-color: #c8c8c8; }
.monaco-editor .tokens-inspect-widget { background-color: #f3f3f3; }
.monaco-editor .tokens-inspect-widget { color: #616161; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e51400'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e9a700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%2375beff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.467; }
.monaco-editor .squiggly-inline-deprecated { text-decoration: line-through; text-decoration-color: #000000}
.monaco-diff-editor .diff-review-line-number { color: #237893; }
.monaco-diff-editor .diff-review-shadow { box-shadow: #dddddd 0 -6px 6px -6px inset; }
.monaco-editor .line-insert, .monaco-editor .char-insert { background-color: rgba(155, 185, 85, 0.2); }
.monaco-diff-editor .line-insert, .monaco-diff-editor .char-insert { background-color: rgba(155, 185, 85, 0.2); }
.monaco-editor .inline-added-margin-view-zone { background-color: rgba(155, 185, 85, 0.2); }
.monaco-editor .line-delete, .monaco-editor .char-delete { background-color: rgba(255, 0, 0, 0.2); }
.monaco-diff-editor .line-delete, .monaco-diff-editor .char-delete { background-color: rgba(255, 0, 0, 0.2); }
.monaco-editor .inline-deleted-margin-view-zone { background-color: rgba(255, 0, 0, 0.2); }
.monaco-diff-editor.side-by-side .editor.modified { box-shadow: -6px 0 5px -5px #dddddd; }
.monaco-editor .bracket-match { background-color: rgba(0, 100, 0, 0.1); }
.monaco-editor .bracket-match { border: 1px solid #b9b9b9; }
.monaco-editor .monaco-editor-overlaymessage .anchor { border-top-color: #007acc; }
.monaco-editor .monaco-editor-overlaymessage .message { border: 1px solid #007acc; }
.monaco-editor .monaco-editor-overlaymessage .message { background-color: #d6ecf2; }

		.monaco-editor .contentWidgets .codicon-lightbulb {
			color: #ddb100;
		}

		.monaco-editor .contentWidgets .codicon-lightbulb-autofix {
			color: #007acc;
		}
.monaco-editor .findOptionsWidget { background-color: #f3f3f3; }
.monaco-editor .findOptionsWidget { color: #616161; }
.monaco-editor .findOptionsWidget { box-shadow: 0 2px 8px #a8a8a8; }
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #a8ac94; }
.monaco-editor .findScope { background-color: rgba(180, 180, 180, 0.3); }
.monaco-editor .find-widget { background-color: #f3f3f3; }
.monaco-editor .find-widget { box-shadow: 0 2px 8px #a8a8a8; }
.monaco-editor .find-widget { color: #616161; }
.monaco-editor .find-widget.no-results .matchesCount { color: #a1260d; }
.monaco-editor .find-widget .monaco-sash { background-color: #c8c8c8; width: 3px !important; margin-left: -4px;}
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: rgba(0, 122, 204, 0.4); }
.monaco-editor .folded-background { background-color: rgba(173, 214, 255, 0.3); }
.monaco-editor .reference-zone-widget .ref-tree .referenceMatch .highlight { background-color: rgba(234, 92, 0, 0.3); }
.monaco-editor .reference-zone-widget .preview .reference-decoration { background-color: rgba(245, 216, 2, 0.87); }
.monaco-editor .reference-zone-widget .ref-tree { background-color: #f3f3f3; }
.monaco-editor .reference-zone-widget .ref-tree { color: #646465; }
.monaco-editor .reference-zone-widget .ref-tree .reference-file { color: #1e1e1e; }
.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .monaco-list-rows > .monaco-list-row.selected:not(.highlighted) { background-color: rgba(51, 153, 255, 0.2); }
.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .monaco-list-rows > .monaco-list-row.selected:not(.highlighted) { color: #6c6c6c !important; }
.monaco-editor .reference-zone-widget .preview .monaco-editor .monaco-editor-background,.monaco-editor .reference-zone-widget .preview .monaco-editor .inputarea.ime-input {	background-color: #f2f8fc;}
.monaco-editor .reference-zone-widget .preview .monaco-editor .margin {	background-color: #f2f8fc;}
.monaco-editor .goto-definition-link { color: #0000ff !important; }
.monaco-editor .marker-widget a { color: #006ab1; }
.monaco-editor .marker-widget a.code-link span:hover { color: #006ab1; }
.monaco-editor-hover .hover-contents a.code-link span:hover { color: #006ab1; }
.monaco-editor .hoverHighlight { background-color: rgba(173, 214, 255, 0.15); }
.monaco-editor .monaco-editor-hover { background-color: #f3f3f3; }
.monaco-editor .monaco-editor-hover { border: 1px solid #c8c8c8; }
.monaco-editor .monaco-editor-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-editor-hover hr { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-editor-hover hr { border-bottom: 0px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-editor-hover a { color: #006ab1; }
.monaco-editor .monaco-editor-hover { color: #616161; }
.monaco-editor .monaco-editor-hover .hover-row .actions { background-color: #e7e7e7; }
.monaco-editor .monaco-editor-hover code { background-color: rgba(220, 220, 220, 0.4); }
.monaco-editor.vs .valueSetReplacement { outline: solid 2px #b9b9b9; }
.monaco-editor .detected-link-active { color: #0000ff !important; }
.monaco-editor .parameter-hints-widget { border: 1px solid #c8c8c8; }
.monaco-editor .parameter-hints-widget.multiple .body { border-left: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .parameter-hints-widget .signature.has-docs { border-bottom: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .parameter-hints-widget { background-color: #f3f3f3; }
.monaco-editor .parameter-hints-widget a { color: #006ab1; }
.monaco-editor .parameter-hints-widget { color: #616161; }
.monaco-editor .parameter-hints-widget code { background-color: rgba(220, 220, 220, 0.4); }
.monaco-editor .snippet-placeholder { background-color: rgba(10, 50, 100, 0.2); outline-color: transparent; }
.monaco-editor .finish-snippet-placeholder { background-color: transparent; outline-color: rgba(10, 50, 100, 0.5); }
.codicon-symbol-array { color: #616161 !important; }
.codicon-symbol-boolean { color: #616161 !important; }
.codicon-symbol-class { color: #d67e00 !important; }
.codicon-symbol-method { color: #652d90 !important; }
.codicon-symbol-color { color: #616161 !important; }
.codicon-symbol-constant { color: #616161 !important; }
.codicon-symbol-constructor { color: #652d90 !important; }

			.codicon-symbol-value,.codicon-symbol-enum { color: #d67e00 !important; }
.codicon-symbol-enum-member { color: #007acc !important; }
.codicon-symbol-event { color: #d67e00 !important; }
.codicon-symbol-field { color: #007acc !important; }
.codicon-symbol-file { color: #616161 !important; }
.codicon-symbol-folder { color: #616161 !important; }
.codicon-symbol-function { color: #652d90 !important; }
.codicon-symbol-interface { color: #007acc !important; }
.codicon-symbol-key { color: #616161 !important; }
.codicon-symbol-keyword { color: #616161 !important; }
.codicon-symbol-module { color: #616161 !important; }
.codicon-symbol-namespace { color: #616161 !important; }
.codicon-symbol-null { color: #616161 !important; }
.codicon-symbol-number { color: #616161 !important; }
.codicon-symbol-object { color: #616161 !important; }
.codicon-symbol-operator { color: #616161 !important; }
.codicon-symbol-package { color: #616161 !important; }
.codicon-symbol-property { color: #616161 !important; }
.codicon-symbol-reference { color: #616161 !important; }
.codicon-symbol-snippet { color: #616161 !important; }
.codicon-symbol-string { color: #616161 !important; }
.codicon-symbol-struct { color: #616161 !important; }
.codicon-symbol-text { color: #616161 !important; }
.codicon-symbol-type-parameter { color: #616161 !important; }
.codicon-symbol-unit { color: #616161 !important; }
.codicon-symbol-variable { color: #007acc !important; }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-highlighted-label .highlight { color: #0066bf; }
.monaco-editor .suggest-widget { color: #000000; }
.monaco-editor .suggest-widget a { color: #006ab1; }
.monaco-editor .suggest-widget code { background-color: rgba(220, 220, 220, 0.4); }
.monaco-editor .accessibilityHelpWidget { background-color: #f3f3f3; }
.monaco-editor .accessibilityHelpWidget { color: #616161; }
.monaco-editor .accessibilityHelpWidget { box-shadow: 0 2px 8px #a8a8a8; }
.monaco-editor .focused .selectionHighlight { background-color: rgba(173, 214, 255, 0.3); }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.15); }
.monaco-editor .wordHighlight { background-color: rgba(87, 87, 87, 0.25); }
.monaco-editor .wordHighlightStrong { background-color: rgba(14, 99, 156, 0.25); }

.mtk1 { color: #000000; }
.mtk2 { color: #fffffe; }
.mtk3 { color: #808080; }
.mtk4 { color: #ff0000; }
.mtk5 { color: #0451a5; }
.mtk6 { color: #0000ff; }
.mtk7 { color: #098658; }
.mtk8 { color: #008000; }
.mtk9 { color: #dd0000; }
.mtk10 { color: #383838; }
.mtk11 { color: #cd3131; }
.mtk12 { color: #863b00; }
.mtk13 { color: #af00db; }
.mtk14 { color: #800000; }
.mtk15 { color: #e00000; }
.mtk16 { color: #3030c0; }
.mtk17 { color: #666666; }
.mtk18 { color: #778899; }
.mtk19 { color: #ff00ff; }
.mtk20 { color: #a31515; }
.mtk21 { color: #4f76ac; }
.mtk22 { color: #008080; }
.mtk23 { color: #001188; }
.mtk24 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }</style><style type="text/css" media="screen">
		.monaco-editor .codelens-decoration.ee1f61 { height: 20px; line-height: 18px; font-size: 11px; padding-right: 5px;}
		.monaco-editor .codelens-decoration.ee1f61 > a > .codicon { line-height: 18px; font-size: 11px; }
		</style></head>
    <!--end::Head-->
    <!--begin::Body-->
    <body id="kt_body" class="header-fixed header-mobile-fixed subheader-enabled subheader-fixed aside-enabled aside-fixed aside-minimize-hoverable loading-overlay-showing" style="background-color: rgb(255, 255, 255);"><div id="MathJax_Message" style="display: none;"></div>
       
        
        <!-- 소프티어 코드 IDE START -->
        <div id="PAGE" class="ide-wrap" data-language="python" data-is_test="">
        <div class="ide-header">
            <h1 style="margin-top:-10px;"><a href="/index.do"><img src="/images/common/logo.png" alt=""></a></h1>
            
            <div class="info">
                <div>
                    <input type="radio" id="color-dark" name="color-theme" class="none">
                    <label for="color-dark" class="info-txt" onclick="chooseColor('dark')" style="margin-bottom: 0px;">dark</label>
                    <input type="radio" id="color-light" name="color-theme" checked="checked" class="none">
                    <label for="color-light" class="info-txt last" onclick="chooseColor('light')" style="margin-bottom: 0px;">light</label>
                </div>
                <div>
                    <span class="info-tit">Font size</span>
                    <select id="code_editor_font_size" class="select3 info-txt" style="width:70px;">
                        <option value="8">8</option>
                        <option value="10">10</option>
                        <option value="12">12</option>
                        <option value="14" selected="selected">14</option>
                        <option value="16">16</option>
                        <option value="18">18</option>
                    </select>
                </div>
                <div>
                    <span class="info-tit">Language</span>
                    <span>
                        <select class="info-txt language select3 option_item" id="submission_language_531">
                            
                                
                                <option value="gnu-c11" data-languagesn="SW_LANG_2" data-language="gnu-c11">GNU C11</option>
                            
                                
                                <option value="gnu-cpp17" data-languagesn="SW_LANG_4" data-language="gnu-cpp17">GNU C++17</option>
                            
                                
                                <option value="openjdk-java-11" data-languagesn="SW_LANG_6" data-language="openjdk-java-11">OpenJDK Java 11</option>
                            
                                <option value="pypy3" data-languagesn="SW_LANG_9" data-language="pypy3" selected="selected">Pypy 7.3 (Python 3.6)</option>
                                
                                                    
                        </select>
                    </span>
                </div>
                
                    <div class="limit_time" data-idx="1258" data-end-time="2021-08-28 15:00:00.0">
                        <span class="info-tit">남은시간</span>
                        <span class="info-txt type01 option_item value">13분 59초 </span>
                    </div>
                
                <div>
                    <span class="info-tit">
                    <!-- <a href="javscript:goApiDocs();" target="_blank"><img alt="API DOCS" src="/images/new/ico_certi1.png" height="32px" width="32px" ></a> -->
                    
                    
                    
                    <a href="https://docs.python.org/3.6/" target="_blank" class="docs bubble-item">API DOCS</a><div class="bubble-box type-docs">선택하신 언어의 공식 DOCS입니다.<br>기본 문법을 확인할 수 있습니다.</div>
                    
                        
                    </span>
                </div>
                
            </div>
        </div>
        <div class="ide-body">
            <div class="ide-head">
                <h2 class="tit">사물인식 최소 면적 산출 프로그램</h2>
                
                
            </div>
            <div class="ide-content">
                <div class="ide-aside section pratice ui-resizable" id="SfproblemForm">
                    <!-- 문제 내용 출력 -->
                    
                    
                                          
                    <div class="v-tit"> 제한시간 : C/C++(2초), Java/Python(5초) | 메모리 제한 : 256MB 
</div><p><br></p><div class="v-txt">
현대자동차그룹에 입사한 당신은 레이더 기술을 활용해 차량 주변의 장애물과 사물을 인식하는 프로그램을 만드는 업무를 담당하고 있다.<br><br><img src="https://www.softeer.ai/upload/2021/07/20210716_093029429_53544.png" title="" alt="" border="0" style="width: 500px; height: 279px; border: 0px solid rgb(0, 0, 0);"><br><br>
당신은 다양한 입력 값들로 인식된 사물에 대해 최소 면적을 계산해보는 테스트를 하는 중이다.<br>
이번 테스트의 조건은 다음과 같다.<br><br>
레이더를 통해 인식된 정보의 입력값은 평면에 N개의 점으로 주어진다.<br> 
각각의 점들은 총 K개의 색깔 중 하나를 가지고 있다.<br> 
각 점의 색깔은 {1, 2, …, K} 중의 한 정수로 표현된다.<br><br>
당신은 입력값으로 주어진 K개의 색깔 {1, 2, …, K}에 대해 해당 색깔을 가지는 점들을 적어도 하나씩 포함하는 사물 중 넓이가 가장 작은 것을 찾아서 그 넓이를 출력하는 프로그램을 작성하려고 한다.<br>
이때, 각 점을 포함한 사물은 반드시 직사각형으로 인식된다.<br><br>
여기서 사물로 인식되는 직사각형은 네 변이 모두 수평 혹은 수직인 것에 한정하며, 직사각형의 내부가 아닌 경계에 놓은 점들도 그 직사각형에 포함된다고 생각한다. 직사각형의 가로 또는 세로의 길이가 0이 되어 선분 혹은 점으로 나타나는 경우도 직사각형의 한 경우로 생각하며 이런 경우 직사각형의(사물) 넓이는 0이다. (하나의 좌표에 여려개의 점이 있을 수 있다)
<br><br>
주어지는 입력값에 대해 K개의 색을 가진 점들을 적어도 하나씩 포함하는 사물(직사각형) 중 넓이가 가장 작은 것의 넓이를 출력하는 프로그램을 만들어보자.</div><p><br></p><div class="v-tit">입력형식</div><div class="v-txt">
입력으로는 점의 개수인 자연수 N과 각 점들이 가질 수 있는 색깔의 총 개수인 자연수 K가 첫 줄에 주어진다.<br>
(1 ≤ N ≤ 100, 1 ≤ K ≤ 20)<br><br>
이후 N줄에는 입력으로 주어지는 점의 좌표 (x, y)와 그 점의 색깔 k가 세 개의 정수 x, y, k로 각 줄에 주어진다.<br>
(-1,000 ≤ x, y ≤ 1,000, 1 ≤ k ≤ K)
</div><p><br></p><div class="v-tit">출력형식</div><div class="v-txt">
주어진 입력에 대해 K개의 색깔 {1, 2, …, K} 각각에 대해 해당 색깔을 가지는 점들을 적어도 하나씩 포함하는 사물(직사각형) 중 넓이가 가장 작은 것을 찾아서 그 넓이를 정수 형태로 출력한다.
</div><p><br></p><div class="v-tit">입력예제 1</div><div class="v-txt v-example">5 2<br>
-4 -2 1<br>
-5 -3 1<br>
5 -4 2<br>
4 -5 2<br>
3 -8 2
</div><p><br></p><div class="v-tit">출력예제 1</div><div class="v-txt v-example">
10
</div><p><br></p><div class="v-tit">입력예제 2</div><div class="v-txt v-example">5 3<br>
3 7 1<br>
5 8 1<br>
6 5 2<br>
7 1 3<br>
9 3 3
</div><p><br></p><div class="v-tit">출력예제 2</div><div class="v-txt v-example">
14
</div><p><br></p><div class="v-tit">입력예제 3</div><div class="v-txt v-example">7 3<br>
-4 0 1<br>
-5 -1 1<br>
0 43 2<br>
3 23 3<br>
8 -19 2<br>
10 0 3<br>
20 0 2
</div><p><br></p><div class="v-tit">출력예제 3</div><div class="v-txt v-example">
0
</div><p><br></p><div class="v-tit">입력예제 4</div><div class="v-txt v-example">
3 3<br>
1 1 1<br>
1 1 2<br>
1 1 3
</div><p><br></p><div class="v-tit">출력예제 4</div><div class="v-txt v-example">
0
</div><p><br></p><div class="v-tit">예제 부연 설명</div><div class="v-txt">
예를 들어, 점의 개수(N)는 5이며, 점의 색깔(K)은 2가지로 좌표평면상 아래와 같이 점이 입력되었다고 할 때, 최소한 다른 색깔의 점을 하나 이상 포함하는 직사각형(사물) 중 가장 작은 면적은 10임을 알 수 있다. <br><br><img src="https://www.softeer.ai/upload/2021/08/20210820_100906597_75799.png" title="" alt="" border="0" style="width: 500px; height: 443px; border: 0px solid rgb(0, 0, 0);"><br><br>
또한 점의 개수(N)는 5이며, 점의 색깔(K)은 3가지로 좌표평면상 아래와 같이 점이 입력되었다고 할 때, 최소한 다른 색깔의 점을 하나 이상 포함하는 직사각형(사물) 중 가장 작은 면적은 14임을 알 수 있다.<br><br><img src="https://www.softeer.ai/upload/2021/08/20210820_101405221_07887.png" title="" alt="" border="0" style="width: 500px; height: 443px; border: 0px solid rgb(0, 0, 0);"><br></div><p><br></p>
                    <!-- 문제 내용 출력 end -->
                </div>
                <div class="ide-resize" data-type="hor"></div>
                <div class="ide-view" style="width: 750.703px; height: 398px;">
                    <div id="code_editor" class="textarea2" data-keybinding-context="1" data-mode-id="python"><div class="monaco-editor no-user-select mac  showUnused vs" data-uri="inmemory://model/1" style="width: 751px; height: 398px;"><div data-mprt="3" class="overflow-guard" style="width: 751px; height: 398px;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; height: 1190px; width: 62px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 1190px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; width: 62px; font-family: Hack, monospace; font-weight: normal; font-size: 12px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 18px; letter-spacing: 0px; height: 1190px;"><div style="position:absolute;top:0px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">1</div></div><div style="position:absolute;top:18px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">2</div></div><div style="position:absolute;top:36px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">3</div></div><div style="position:absolute;top:54px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">4</div></div><div style="position:absolute;top:72px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">5</div></div><div style="position:absolute;top:90px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">6</div></div><div style="position:absolute;top:108px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">7</div></div><div style="position:absolute;top:126px;width:100%;height:18px;"><div class="cldr codicon codicon-chevron-down" style="left:36px;width:26px;"></div><div class="line-numbers" style="left:0px;width:36px;">8</div></div><div style="position:absolute;top:144px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">9</div></div><div style="position:absolute;top:162px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">10</div></div><div style="position:absolute;top:180px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">11</div></div><div style="position:absolute;top:198px;width:100%;height:18px;"><div class="cldr codicon codicon-chevron-down" style="left:36px;width:26px;"></div><div class="line-numbers" style="left:0px;width:36px;">12</div></div><div style="position:absolute;top:216px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">13</div></div><div style="position:absolute;top:234px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">14</div></div><div style="position:absolute;top:252px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">15</div></div><div style="position:absolute;top:270px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">16</div></div><div style="position:absolute;top:288px;width:100%;height:18px;"><div class="cldr codicon codicon-chevron-down" style="left:36px;width:26px;"></div><div class="line-numbers" style="left:0px;width:36px;">17</div></div><div style="position:absolute;top:306px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">18</div></div><div style="position:absolute;top:324px;width:100%;height:18px;"><div class="cldr codicon codicon-chevron-down" style="left:36px;width:26px;"></div><div class="line-numbers" style="left:0px;width:36px;">19</div></div><div style="position:absolute;top:342px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">20</div></div><div style="position:absolute;top:360px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">21</div></div><div style="position:absolute;top:378px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">22</div></div><div style="position:absolute;top:396px;width:100%;height:18px;"><div class="line-numbers" style="left:0px;width:36px;">23</div></div></div></div><div class="monaco-scrollable-element editor-scrollable vs mac" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 62px; width: 689px; height: 398px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 1e+06px; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; height: 0px; width: 689px;"><div style="position:absolute;top:0px;width:100%;height:18px;"></div><div style="position:absolute;top:18px;width:100%;height:18px;"></div><div style="position:absolute;top:36px;width:100%;height:18px;"></div><div style="position:absolute;top:54px;width:100%;height:18px;"></div><div style="position:absolute;top:72px;width:100%;height:18px;"></div><div style="position:absolute;top:90px;width:100%;height:18px;"></div><div style="position:absolute;top:108px;width:100%;height:18px;"></div><div style="position:absolute;top:126px;width:100%;height:18px;"></div><div style="position:absolute;top:144px;width:100%;height:18px;"><div class="cigr" style="left:0px;height:18px;width:28.90625px"></div></div><div style="position:absolute;top:162px;width:100%;height:18px;"><div class="cigr" style="left:0px;height:18px;width:28.90625px"></div></div><div style="position:absolute;top:180px;width:100%;height:18px;"></div><div style="position:absolute;top:198px;width:100%;height:18px;"></div><div style="position:absolute;top:216px;width:100%;height:18px;"><div class="cigr" style="left:0px;height:18px;width:28.90625px"></div></div><div style="position:absolute;top:234px;width:100%;height:18px;"><div class="cigr" style="left:0px;height:18px;width:28.90625px"></div></div><div style="position:absolute;top:252px;width:100%;height:18px;"><div class="cigr" style="left:0px;height:18px;width:28.90625px"></div></div><div style="position:absolute;top:270px;width:100%;height:18px;"></div><div style="position:absolute;top:288px;width:100%;height:18px;"></div><div style="position:absolute;top:306px;width:100%;height:18px;"><div class="cigr" style="left:0px;height:18px;width:28.90625px"></div></div><div style="position:absolute;top:324px;width:100%;height:18px;"><div class="cigr" style="left:0px;height:18px;width:28.90625px"></div></div><div style="position:absolute;top:342px;width:100%;height:18px;"><div class="cigr" style="left:0px;height:18px;width:28.90625px"></div><div class="cigr" style="left:28.90625px;height:18px;width:28.90625px"></div></div><div style="position:absolute;top:360px;width:100%;height:18px;"><div class="cigr" style="left:0px;height:18px;width:28.90625px"></div><div class="cigr" style="left:28.90625px;height:18px;width:28.90625px"></div></div><div style="position:absolute;top:378px;width:100%;height:18px;"><div class="cigr" style="left:0px;height:18px;width:28.90625px"></div><div class="cigr" style="left:28.90625px;height:18px;width:28.90625px"></div></div><div style="position:absolute;top:396px;width:100%;height:18px;"><div class="cigr" style="left:0px;height:18px;width:28.90625px"></div><div class="cigr" style="left:28.90625px;height:18px;width:28.90625px"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: Hack, monospace; font-weight: normal; font-size: 12px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 18px; letter-spacing: 0px; width: 689px; height: 1190px;"><div style="top:0px;height:18px;" class="view-line"><span><span class="mtk6">import</span><span class="mtk1">&nbsp;sys</span></span></div><div style="top:18px;height:18px;" class="view-line"><span><span>&nbsp;</span></span></div><div style="top:36px;height:18px;" class="view-line"><span><span class="mtk8">#&nbsp;좌표들&nbsp;정렬하고,&nbsp;기준&nbsp;하나&nbsp;잡고&nbsp;오른쪽으로&nbsp;탐색하기</span></span></div><div style="top:54px;height:18px;" class="view-line"><span><span>&nbsp;</span></span></div><div style="top:72px;height:18px;" class="view-line"><span><span class="mtk1">n,&nbsp;k&nbsp;=&nbsp;</span><span class="mtk6">map</span><span class="mtk1">(</span><span class="mtk6">int</span><span class="mtk1">,&nbsp;</span><span class="mtk6">input</span><span class="mtk1">().split())</span></span></div><div style="top:90px;height:18px;" class="view-line"><span><span>&nbsp;</span></span></div><div style="top:108px;height:18px;" class="view-line"><span><span class="mtk1">COLOR&nbsp;=&nbsp;[&nbsp;[]&nbsp;</span><span class="mtk6">for</span><span class="mtk1">&nbsp;_&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;</span><span class="mtk6">range</span><span class="mtk1">(k&nbsp;+&nbsp;</span><span class="mtk7">1</span><span class="mtk1">)]</span></span></div><div style="top:126px;height:18px;" class="view-line"><span><span class="mtk6">for</span><span class="mtk1">&nbsp;_&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;</span><span class="mtk6">range</span><span class="mtk1">(n):</span></span></div><div style="top:144px;height:18px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;y,&nbsp;x,&nbsp;color&nbsp;=&nbsp;</span><span class="mtk6">map</span><span class="mtk1">(</span><span class="mtk6">int</span><span class="mtk1">,&nbsp;</span><span class="mtk6">input</span><span class="mtk1">().split())</span></span></div><div style="top:162px;height:18px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;COLOR[color].append((y,&nbsp;x))</span></span></div><div style="top:180px;height:18px;" class="view-line"><span><span>&nbsp;</span></span></div><div style="top:198px;height:18px;" class="view-line"><span><span class="mtk1">ans&nbsp;=&nbsp;</span><span class="mtk7">1e9</span></span></div><div style="top:216px;height:18px;" class="view-line"><span><span>&nbsp;</span></span></div><div style="top:234px;height:18px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;a&nbsp;b</span></span></div><div style="top:252px;height:18px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;c&nbsp;d</span></span></div><div style="top:270px;height:18px;" class="view-line"><span><span>&nbsp;</span></span></div><div style="top:288px;height:18px;" class="view-line"><span><span class="mtk6">def</span><span class="mtk1">&nbsp;rec(cur,&nbsp;A,&nbsp;B,&nbsp;C,&nbsp;D):</span></span></div><div style="top:306px;height:18px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk6">global</span><span class="mtk1">&nbsp;k,&nbsp;ans</span></span></div><div style="top:324px;height:18px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk6">if</span><span class="mtk1">&nbsp;cur&nbsp;==&nbsp;k&nbsp;+&nbsp;</span><span class="mtk7">1</span><span class="mtk1">:</span></span></div><div style="top:342px;height:18px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;print(A,&nbsp;B,&nbsp;C,&nbsp;D,&nbsp;sep&nbsp;=&nbsp;'\n')</span></span></div><div style="top:360px;height:18px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area&nbsp;=&nbsp;</span><span class="mtk6">abs</span><span class="mtk1">(C[</span><span class="mtk7">0</span><span class="mtk1">]&nbsp;-&nbsp;A[</span><span class="mtk7">0</span><span class="mtk1">])&nbsp;*&nbsp;</span><span class="mtk6">abs</span><span class="mtk1">(B[</span><span class="mtk7">1</span><span class="mtk1">]&nbsp;-&nbsp;A[</span><span class="mtk7">1</span><span class="mtk1">])</span></span></div><div style="top:378px;height:18px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;print(area)</span></span></div><div style="top:396px;height:18px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ans&nbsp;=&nbsp;</span><span class="mtk6">min</span><span class="mtk1">(ans,&nbsp;area)</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor " style="height: 18px; top: 0px; left: 0px; font-family: Hack, monospace; font-weight: normal; font-size: 12px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 18px; letter-spacing: 0px; display: block; visibility: hidden; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 675px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 675px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="28" height="796" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 398px;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical fade" style="position: absolute; width: 14px; height: 398px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 133px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 751px;"></div><textarea data-mprt="6" class="inputarea" wrap="off" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." role="textbox" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="font-family: Hack, monospace; font-weight: normal; font-size: 12px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 18px; letter-spacing: 0px; top: 0px; left: 62px; width: 1px; height: 18px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 751px;"><div class="accessibilityHelpWidget" role="dialog" aria-hidden="true" widgetid="editor.contrib.accessibilityHelpWidget" style="display: none; position: absolute;"><div role="document"></div></div><div class="monaco-editor-hover hidden" aria-hidden="true" role="presentation" widgetid="editor.contrib.modesGlyphHoverWidget" style="position: absolute;"></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 398px;"><div class="minimap-shadow-hidden" style="height: 398px;"></div><canvas width="0" height="796" style="position: absolute; left: 0px; width: 0px; height: 398px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="796" style="position: absolute; left: 0px; width: 0px; height: 398px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div></div><div data-mprt="2" class="overflowingContentWidgets"><div class="monaco-editor rename-box" widgetid="__renameInputWidget" style="background-color: rgb(243, 243, 243); box-shadow: rgb(168, 168, 168) 0px 2px 8px; color: rgb(97, 97, 97); position: absolute; visibility: hidden; max-width: 1388px;"><input class="rename-input" type="text" aria-label="Rename input. Type new name and press Enter to commit." style="font-family: Hack, monospace; font-weight: normal; font-size: 12px; background-color: rgb(255, 255, 255); border-width: 0px; border-style: none;"><div class="rename-label" style="font-size: 9.6px;">Enter to Rename, ⇧Enter to Preview</div></div><div class="editor-widget suggest-widget" widgetid="editor.widget.suggestWidget" style="position: absolute; visibility: inherit; max-width: 1118px; top: 18px; left: 62px;" monaco-visible-content-widget="true"><div class="message" aria-hidden="true" style="display: none; background-color: rgb(243, 243, 243); border-color: rgb(200, 200, 200);"></div><div class="tree" aria-hidden="true" style="display: none; background-color: rgb(243, 243, 243); border-color: rgb(200, 200, 200);"><div class="monaco-list list_id_1" tabindex="0" role="tree"><div class="monaco-scrollable-element  mac" role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-list-rows" style="transform: translate3d(0px, 0px, 0px); overflow: hidden;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div></div><style type="text/css" media="screen">.monaco-list.list_id_1:focus .monaco-list-row.focused { background-color: #d6ebff; }
.monaco-list.list_id_1:focus .monaco-list-row.focused:hover { background-color: #d6ebff; }
.monaco-list.list_id_1:focus .monaco-list-row.selected { background-color: #0069d1; }
.monaco-list.list_id_1:focus .monaco-list-row.selected:hover { background-color: #0069d1; }
.monaco-list.list_id_1:focus .monaco-list-row.selected { color: #ffffff; }

				.monaco-drag-image,
				.monaco-list.list_id_1:focus .monaco-list-row.selected.focused { background-color: #0074e8; }
			

				.monaco-drag-image,
				.monaco-list.list_id_1:focus .monaco-list-row.selected.focused { color: #ffffff; }
			
.monaco-list.list_id_1 .monaco-list-row.focused { background-color:  #d6ebff; }
.monaco-list.list_id_1 .monaco-list-row.focused:hover { background-color:  #d6ebff; }
.monaco-list.list_id_1 .monaco-list-row.selected { background-color:  #e4e6f1; }
.monaco-list.list_id_1 .monaco-list-row.selected:hover { background-color:  #e4e6f1; }
.monaco-list.list_id_1:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color:  #f0f0f0; }

				.monaco-list.list_id_1.drop-target,
				.monaco-list.list_id_1 .monaco-list-rows.drop-target,
				.monaco-list.list_id_1 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; }
			
.monaco-list-type-filter { background-color: #efc1ad }
.monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); }
.monaco-list-type-filter.no-matches { border: 1px solid #be1100; }
.monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }</style></div></div><div class="suggest-status-bar" aria-hidden="true" style="display: none; background-color: rgb(243, 243, 243); border-color: rgb(200, 200, 200);"><span></span><span></span></div><div class="details" aria-hidden="true" style="font-size: 12px; font-weight: normal; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; display: none; background-color: rgb(243, 243, 243); border-color: rgb(200, 200, 200);"><div class="monaco-scrollable-element  mac" role="presentation" style="position: relative; overflow: hidden;"><div class="body" style="overflow: hidden;"><div class="header"><span class="codicon codicon-close" title="Read less...⌃Space" style="height: 18px; width: 18px;"></span><p class="type" style="font-family: Hack, monospace;"></p></div><p class="docs"></p></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow top-left-corner"></div></div></div></div><div class="monaco-editor-hover hidden" tabindex="0" widgetid="editor.contrib.modesContentHoverWidget" style="position: absolute; visibility: hidden; max-width: 1388px;"><div class="monaco-scrollable-element  mac" role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-editor-hover-content" style="overflow: hidden; font-size: 12px; line-height: 18px; max-height: 250px; max-width: 500px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow top-left-corner"></div></div></div></div><div class="context-view" aria-hidden="true" style="display: none;"></div></div></div>
                    <div class="ide-animation" style="display:none;">
                        <span class="circle"></span>
                        <span class="submit-img"></span>
                    </div>
                    <div class="ide-resize type01" data-type="ver"></div>
                    <div class="ide-view-menu">
                        <div class="ide-menu-name">
                        계산기
                            <input type="checkbox" id="calc-chk" class="calc-chk btn_on_off"><label for="calc-chk" onclick="calcOnOff()">계산기 사용</label>
                        </div>
                        
                        <ul class="btn-list console">
                            
                            <li>
                                <button class="btn_save btn-type5 bubble-item" data-eventidx="1258" data-psproblemid="531" data-language="pypy3" data-groupid="G00001" data-practiceid="SW_PRBL_719" data-languagesn="SW_LANG_9" data-eventtype="certification">임시저장</button>
                                <div class="bubble-box" style="width: 278px;">
                                  작성 코드를 저장합니다. 주기적으로 저장해주세요.
                                </div>
                            </li>
                            <li>
                                <button class="btn_test btn-type5 bubble-item">코드실행</button>
                                <div class="bubble-box" style="width: 295px; left:43%">
                                  작성 코드를 제출하기 전에 먼저 실행해볼 수 있습니다.
                                </div>
                            </li>
                            <li>
                                <button class="btn-type5 btn_console_clear bubble-item">초기화</button>
                                <div class="bubble-box" style="width: 182px; left:82%">
                                  코드실행 결과를 모두 지웁니다.
                                </div>
                            </li>
                            <li>
                                
                                    
                                    
                                    
                                        <button class="btn_submit btn-type4 bubble-item" data-eventidx="1258" data-psproblemid="531" data-language="pypy3" data-groupid="G00001" data-practiceid="SW_PRBL_719" data-languagesn="SW_LANG_9" data-eventtype="certification">코드제출</button>
                                    
                                
                                <div class="bubble-box" style="left: -5%; width: 269px;" id="submitCn">
                                  테스트 종료 전까지 언제든 다시 제출할 수 있으며 가장 마지막에 제출한 코드가 최종 답안이 됩니다.
                                </div>
                            </li>
                        </ul>
                        </div>
                       <div class="ide-view-aside" style="height: 320px;">
                       <div id="calculator" class="ide-calc off"><div class="history" style="display:none;"></div><table id="coForward_calculator" class="off CF_calculator_btn_area"><tbody><tr><td colspan="4" class="calc-view display" data-number="0">0</td></tr><tr><td><button class="calc-back" type="button" data-function="Backspace" disabled="disabled">backspace</button></td><td><button type="button" data-function="/" disabled="disabled">/</button></td><td><button type="button" data-function="*" disabled="disabled">*</button></td><td><button type="button" data-function="-" disabled="disabled">-</button></td></tr><tr><td><button type="button" data-number="7" disabled="disabled">7</button></td><td><button type="button" data-number="8" disabled="disabled">8</button></td><td><button type="button" data-number="9" disabled="disabled">9</button></td><td rowspan="2"><button type="button" data-function="+" disabled="disabled">+</button></td></tr><tr><td><button type="button" data-number="4" disabled="disabled">4</button></td><td><button type="button" data-number="5" disabled="disabled">5</button></td><td><button type="button" data-number="6" disabled="disabled">6</button></td></tr><tr><td><button type="button" data-number="1" disabled="disabled">1</button></td><td><button type="button" data-number="2" disabled="disabled">2</button></td><td><button type="button" data-number="3" disabled="disabled">3</button></td><td rowspan="2"><button data-function="Enter" disabled="disabled">Enter</button></td></tr><tr><td colspan="2"><button type="button" data-number="0" disabled="disabled">0</button></td><td><button type="button" data-number="." disabled="disabled">.</button></td></tr></tbody></table><div class="calc-info CF_calculator_btn_area"><input type="checkbox" id="calc-key-chk" class="calc-key-chk" checked="checked"><label for="calc-key-chk">키패드 사용</label><button class="btn-type3" data-function="Escape" disabled="disabled">Reset</button></div></div>
                        
                      <div class="ide-console" id="ide-console">
                        <div id="output" style="width: 100%; padding: 20px; margin-bottom: 0px; overflow-y: scroll;" class="v-txt">
                        </div>
                        <div class="testcase_div ide-console-view" style="display:none;">
                            <ul class="btn-list">  
                                <li>
                                    <button class="btn-type5 btn_run excute" data-eventtype="certification" data-language="pypy3">실행</button>
                                </li>
                                <li>
                                    <button class="btn-type5 btn_run cancel">닫기</button>
                                </li>
                            </ul>
                        <textarea id="testcase" class="ide-console-view-text" placeholder="테스트케이스 추가하기
(미 입력 실행 시, 예제 자동 실행)"></textarea>
                        </div>
                        
                        
                    </div>
                </div>
                </div>
            </div>
        </div>
        <input type="hidden" id="data-eventIdx" value="1258">
        <input type="hidden" id="data-psProblemId" value="531">
        <input type="hidden" id="data-groupId" value="G00001">
        <input type="hidden" id="data-practiceId" value="SW_PRBL_719">
        <input type="hidden" id="data-userName" value="김민재">
        <input type="hidden" id="ide-code" value="import sys

# 좌표들 정렬하고, 기준 하나 잡고 오른쪽으로 탐색하기

n, k = map(int, input().split())

COLOR = [ [] for _ in range(k + 1)]
for _ in range(n):
    y, x, color = map(int, input().split())
    COLOR[color].append((y, x))

ans = 1e9

    # a b
    # c d

def rec(cur, A, B, C, D):
    global k, ans
    if cur == k + 1:
        # print(A, B, C, D, sep = '\n')
        area = abs(C[0] - A[0]) * abs(B[1] - A[1])
        # print(area)
        ans = min(ans, area)
        return

    if cur == 1:
        for y, x in COLOR[cur]:
            a = [y, x]
            b = [y, x]
            c = [y, x]
            d = [y, x]
            rec(cur + 1, a, b, c, d)
    else:
        for y, x in COLOR[cur]:
            a = [ min(A[0], y), min(A[1], x)  ]
            b = [ min(B[0], y), max(B[1], x)  ]
            c = [ max(C[0], y), min(C[1], x)  ]
            d = [ max(D[0], y), max(D[1], x)  ]
            rec(cur + 1, a, b, c, d)




rec(1, -1, -1, -1, -1)
print(ans)

'''