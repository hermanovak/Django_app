//db
// Construct the data object with your variables
document.addEventListener('DOMContentLoaded', function () {
   /* $(function() {
        if (isPost ==0){
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, gtr: gtr},
                success:function(response){},
                error: function (response) {
                    // alert the error if any error occured
                    console.log(response.responseJSON.errors)
                    
                }});
        isPost = 1;
        }
    });*/
    //console.log("/daily"+String(gtr))

    // if (datacheck==1) {
    //     x = window.confirm("Do you want to reload the last test?") 
    //     if (x === true) {
    //         $(function() {
    //             $.ajax({
    //                 type: 'POST',
    //                 url:"/daily"+String(gtr),
    //                 data: {csrfmiddlewaretoken: window.CSRF_TOKEN, reload: 1},
    //                 success:function(response){}});
    //     });
    //     }

    // }

    const MLICenable = document.getElementById("mlic-enable");
    if (MLICenable.checked == false) {document.getElementById("mlic-select").disabled = true};
    MLICenable.addEventListener("change", function () {
        //MLICenable.value = MLICenable.checked;
        if (MLICenable.checked == true) {
            document.getElementById("mlic-select").disabled = false;
        }
        else {document.getElementById("mlic-select").disabled = true}
    })

    const lynxSelect = document.getElementById("lynx-select");
    const lynx = document.getElementById("lynx");
    const lynxLR = document.getElementById("lynxLR");

    const komoraSelect = document.getElementById("komora-select");
    const komora = document.getElementById("komora");
    const komoraLR = document.getElementById("komoraLR");

    komoraSelect.addEventListener("change", function() {
        if (komoraSelect.value == "none") {
            komora.style.display = "none"
        } else {
            komora.style.display = "block"
        }
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, IcID: komoraSelect.value},
                success:function(response){}});
        });
    });

    const mlicSelect = document.getElementById("mlic-select");
    const mlic = document.getElementById("mlic");
    const mlicLR = document.getElementById("mlicLR");
    lynxSelect.addEventListener("change", function() {
        // Show the selected option form
        if (lynxSelect.value === "none") {
            lynx.style.display = "none";
        } else if (lynxSelect.value != "none") {
            lynx.style.display = "block";
        }
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, LynxID: lynxSelect.value},
                success:function(response){console.log(gtr)}});
        });
    });

    mlicSelect.addEventListener("change", function() {
        // Show the selected option form
        if (mlicSelect.value === "none") {
            mlic.style.display = "none";
        } else if (mlicSelect.value != "none") {
            mlic.style.display = "block";
        }
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, MlicID: mlicSelect.value},
                success:function(response){}});
        });
    });

    var dataP = {
    Temp: Temp,
    Pres: Pres,
    Ktp: KtpOut,

    Kpol: KpolOut,
    Ksat: KsatOut,
    Kqq: KqqOut,

    L11595: L11595out,
    L11599: L11599out,
    L115avg: L115avgout,
    L115max: L115maxout,
    L14595: L14595out,
    L14599: L14599out,
    L145avg: L145avgout,
    L145max: L145maxout,
    L22695: L22695out,
    L22699: L22699out,
    L226avg: L226avgout,
    L226max: L226maxout,

    K100D: D100,
    K100: dev100,
    K170D: D170,
    K170: dev170,
    K226D: D226,
    K226: dev226,

    M100R: MLIC100out,
    M100: MLICdev100,
    M170R: MLIC170out,
    M170R: MLICdev170,
    M226R: MLIC226out,
    M226: MLICdev226
    };
    //Send the data to the Django views.py file

    //misc vars declare
    var inputValueTemp;
    var iconTemp;
    var inputValuePres;
    var iconPres;
    var inputValueK;
    var iconK;
    var iconMisc;

    var laserX;
    var laserY;
    var laserZ;
    var flatpanels;
    var DynR;
    var VisionRT;
    var miscChecks0;
    var miscChecksX;
    // var miscVals;

    var Temp;
    var Pres;
    var KtpOut;
    var K;

    // var T;
    // var p;

    var KpolOut;
    var KsatOut;
    var KqqOut;

    // var Ktp;

    var iconAll;
    //lynx vars declare
    var inputValueL11595;
    var iconL11595;
    var inputValueL11599;
    var iconL11599;
    var inputValueL14595;
    var iconL14595;
    var inputValueL14599;
    var iconL14599;
    var inputValueL22695;
    var iconL22695;
    var inputValueL22699;
    var iconL22699;
    var L115avg;
    var L115max;
    var L145avg;
    var L145max;
    var L226avg;
    var L226max;
    //lynx outs
    var L11595out;
    var L11599out;
    var L115avgout;
    var L115maxout;
    var L14595out;
    var L14599out;
    var L145avgout;
    var L145maxout;
    var L22695out;
    var L22699out;
    var L226avgout;
    var L226maxout;
    //komora vars declare
    var inputValueK100nC;
    var inputValueK100mu;
    var iconK100;
    var inputValueK170nC;
    var inputValueK170mu;
    var iconK170;
    var inputValueK226nC;
    var inputValueK226mu;
    var iconK226;
    //komory refs
    var NDW;
    const K3190ndw = 47870000;
    const K3190Ksat = 1.005;
    const K3190Kpol = 1;
    const K2132ndw = 48290000;
    const K2132Ksat = 1.006;
    const K2132Kpol = 1;
    const K3565ndw = 48060000;
    const K3565Ksat = 1.0044;
    const K3565Kpol = 1.0001;
    const K4218ndw = 47900000;
    const K4218Ksat = 1.005;
    const K4218Kpol = 1;
    const K5414ndw = 47880000;
    const K5414Ksat = 1.0052;
    const K5414Kpol = 1;
    const Kqq = 1.035;
    //dose refs
    document.getElementById("K100refD").textContent = K100ref;
    document.getElementById("K170refD").textContent = K170ref;
    document.getElementById("K226refD").textContent = K226ref;
    //komora outs
    var K100outD;
    var K100out;
    var K170outD;
    var K170out;
    var K226outD;
    var K226out;
    //komora calcs
    var K100mu;
    var K100nc;
    var K170mu;
    var K170nc;
    var K226mu;
    var K226nc;
    var D100;
    var dev100;
    var D170;
    var dev170;
    var D226;
    var dev226;
    //mlic refs
    document.getElementById("MLIC100refR").textContent = MLIC100ref;
    document.getElementById("MLIC170refR").textContent = MLIC170ref;
    document.getElementById("MLIC226refR").textContent = MLIC226ref;
    //mlic vars declare
    var MLIC100;
    var MLIC170;
    var MLIC226;
    var iconMLIC100;
    var iconMLIC170;
    var iconMLIC226;
    //mlic refs
    // var MLIC100ref;
    // var MLIC170ref;
    // var MLIC226ref;
    //mlic outs
    var MLIC100out;
    var MLIC170out;
    var MLIC226out;
    //mlic calcs
    var MLICdev100;
    var MLICdev170;
    var MLICdev226;
    //functions
    function MiscUpdate () {
        Temp.value = inputValueTemp.value;
        //console.log(Temp.value+273.15);
        Pres.value = inputValuePres.value;
        K = inputValueK.value;
        //checks na lasers a ine doplnit
    };
    function MiscCalc () {
        Ktp = (((parseFloat(Temp.value) + 273.15) / (273.15 + 20)) * (1013 / parseFloat(Pres.value)));
        KtpOut.value = Ktp;
    };
    function MiscCheck () {
        miscChecksX = document.querySelectorAll('input[type="checkbox"]:checked');
    };
    function DoseCalc () {
        D100 = parseFloat(K100nc) * 100 / parseFloat(K100mu) * parseFloat(NDW) * parseFloat(KtpOut.value) * parseFloat(KsatOut.value) * parseFloat(KpolOut.value) * parseFloat(KqqOut.value) * 1e-9;
        dev100 = ((D100 / K100ref) - 1) * 100;
        D170 = parseFloat(K170nc) * 100 / parseFloat(K170mu-K100mu) * parseFloat(NDW) * parseFloat(KtpOut.value) * parseFloat(KsatOut.value) * parseFloat(KpolOut.value) * parseFloat(KqqOut.value) * 1e-9;
        dev170 = ((D170 / K170ref) - 1) * 100;
        D226 = parseFloat(K226nc) * 100 / parseFloat(K226mu-K170mu) * parseFloat(NDW) * parseFloat(KtpOut.value) * parseFloat(KsatOut.value) * parseFloat(KpolOut.value) * parseFloat(KqqOut.value) * 1e-9;
        dev226 = ((D226 / K226ref) - 1) * 100;
        if (inputValueK100mu.value.length != 0 && inputValueK100nC.value.length != 0) {
            K100outD.textContent = D100;
            K100out.textContent = dev100;
            if (dev100 >= -2 && dev100 <= 2) {
                iconK100.innerHTML = "&#10004;"; // pass icon
                iconK100.style.color = "green";
            } else {
                iconK100.innerHTML = "&#10008;"; // fail icon
                iconK100.style.color = "red";
            };
        } else {
            K100outD.textContent = "";
            K100out.textContent = "";
            iconK100.innerHTML = "";
        }
        if (inputValueK170mu.value.length != 0 && inputValueK170nC.value.length != 0) {
            K170outD.textContent = D170;
            K170out.textContent = dev170;
            if (dev170 >= -2 && dev170 <= 2) {
                iconK170.innerHTML = "&#10004;"; // pass icon
                iconK170.style.color = "green";
            } else {
                iconK170.innerHTML = "&#10008;"; // fail icon
                iconK170.style.color = "red";
            };
        } else {
            K170outD.textContent = "";
            K170out.textContent = "";
            iconK170.innerHTML = "";
        }
        if (inputValueK226mu.value.length != 0 && inputValueK226nC.value.length != 0) {
            K226outD.textContent = D226;
            K226out.textContent = dev226;
            if (dev226 >= -2 && dev226 <= 2) {
                iconK226.innerHTML = "&#10004;"; // pass icon
                iconK226.style.color = "green";
            } else {
                iconK226.innerHTML = "&#10008;"; // fail icon
                iconK226.style.color = "red";
            };
        } else {
            K226outD.textContent = "";
            K226out.textContent = "";
            iconK226.innerHTML = "";
        }
    };
    function MlicCalc () {
        MLICdev100 = parseFloat(MLIC100out.value) - parseFloat(MLIC100ref);
        MLICdev170 = parseFloat(MLIC170out.value) - parseFloat(MLIC170ref);
        MLICdev226 = parseFloat(MLIC226out.value) - parseFloat(MLIC226ref);
        if (MLIC100.value.length != 0) {
            MLIC100out.textContent = MLICdev100;
            if (MLICdev100 >= -0.15 && MLICdev100 <= 0.15) {
                iconMLIC100.innerHTML = "&#10004;"; // pass icon
                iconMLIC100.style.color = "green";
            } else {
                iconMLIC100.innerHTML = "&#10008;"; // fail icon
                iconMLIC100.style.color = "red";
            };
        } else {
            MLIC100out.textContent = "";
            iconMLIC100.innerHTML = "";
        };
        if (MLIC170.value.length != 0) {
            MLIC170out.textContent = MLICdev170;
            if (MLICdev170 >= -0.15 && MLICdev170 <= 0.15) {
                iconMLIC170.innerHTML = "&#10004;"; // pass icon
                iconMLIC170.style.color = "green";
            } else {
                iconMLIC170.innerHTML = "&#10008;"; // fail icon
                iconMLIC170.style.color = "red";
            };
        } else {
            MLIC170out.textContent = "";
            iconMLIC170.innerHTML = "";
        };
        if (MLIC226.value.length != 0) {
            MLIC226out.textContent = MLICdev226;
            if (MLICdev226 >= -0.15 && MLICdev226 <= 0.15) {
                iconMLIC226.innerHTML = "&#10004;"; // pass icon
                iconMLIC226.style.color = "green";
            } else {
                iconMLIC226.innerHTML = "&#10008;"; // fail icon
                iconMLIC226.style.color = "red";
            };
        } else {
            MLIC226out.textContent = "";
            iconMLIC226.innerHTML = "";
        };
    };

    //checkboxes check + check of all checks, czechs number one
    reload = document.getElementById("reload");
    inputValueTemp = document.getElementById("temperature");
    iconTemp = document.getElementById("icon-temp");
    inputValuePres = document.getElementById("pressure");
    iconPres = document.getElementById("icon-press");
    inputValueK = document.getElementById("k");
    iconK = document.getElementById("icon-k");

    laserX = document.getElementById("X");
    laserY = document.getElementById("Y");
    laserZ = document.getElementById("Z");
    flatpanels = document.getElementById("flat-panels");
    VisionRT = document.getElementById("vision");
    DynR = document.getElementById("dynr");
    miscChecks0 = document.querySelectorAll('input[type="checkbox"]:enabled');

    submitB = document.getElementById("submit");

    iconMisc = document.getElementById("icon-misc");
       
    Temp = document.getElementById("tempOut");
    Pres = document.getElementById("presOut");

    KtpOut = document.getElementById("ktpOut");

    KpolOut = document.getElementById("kpolOut");
    KsatOut = document.getElementById("ksatOut");
    KqqOut = document.getElementById("kqqOut");
    console.log(inputValueTemp.value)
    MiscUpdate();
    MiscCalc();
    //DoseCalc ();
    // if (datacheck==1) {
    //     console.log(reload)
    //     if (reload['temperature']!=null) {
    //         inputValueTemp.value = reload['temperature'];}
    // }
    // var count = 0;
    // miscChecks.forEach(check=>{
    //     check.addEventListener("change", function(){
    //         if (check.checked = true) {
    //             count++
    //         }
    //         alert(count)
    //         if (miscChecks.length = count) {
    //             iconMisc.innerHTML = "&#10004;"; // pass icon
    //             iconMisc.style.color = "green";
    //         }
    //     })
    // })
    
    // iconAll = document.getElementById("icon-all");
    // $(function () {
    //     $.ajaxSetup({
    //         headers: { "X-CSRFToken": '{{csrf_token}}' }
    //     });
    // });
    // misc value checks TREBA LOOP THROUGH ALL ELEMENTS

    inputValueTemp.addEventListener("input", function () {
        if (inputValueTemp.value >= 15 && inputValueTemp.value <= 30) {
            iconTemp.innerHTML = "&#10004;"; // pass icon
            iconTemp.style.color = "green";
            var T = parseFloat(inputValueTemp.value) + 273.15;
            //Temp = T
            Temp.textContent = T;
            //Ktp = ((273.15 + Temp.value) / (273.15 + 20) * (1013 / Pres.value));
            //KtpOut.textContent = Ktp;
        } else {
            iconTemp.innerHTML = "&#10008;"; // fail icon
            iconTemp.style.color = "red";
        }
        MiscUpdate();
        MiscCalc();
        DoseCalc ();
        KtpOut.textContent = KtpOut.value;
        });
    inputValueTemp.addEventListener("blur", function(){
        if (inputValueTemp.value >= 15 && inputValueTemp.value <= 30) {
            $(function() {
                $.ajax({
                    type: 'POST',
                    url:"/daily"+String(gtr),
                    data: {csrfmiddlewaretoken: window.CSRF_TOKEN, Temp: Temp.value},
                    success:function(response){}});
            });
        };
    });


    inputValuePres.addEventListener("input", function () {
        if (inputValuePres.value >= 900 && inputValuePres.value <= 1100) {
            iconPres.innerHTML = "&#10004;"; // pass icon
            iconPres.style.color = "green";
            var p = parseFloat(inputValuePres.value);
            //Pres = p;
            Pres.textContent = p;
            
            //Ktp = ((273.15 + Temp.value) / (273.15 + 20) * (1013 / Pres.value));
            //KtpOut.textContent = Ktp;
        } else {
            iconPres.innerHTML = "&#10008;"; // fail icon
            iconPres.style.color = "red";
        }
        MiscUpdate();
        MiscCalc();
        DoseCalc ();
        KtpOut.textContent = KtpOut.value;
        //p = inputValuePres.value;
    });
    inputValuePres.addEventListener("blur", function(){
        if (inputValuePres.value >= 900 && inputValuePres.value <= 1100) {
            $(function() {
                $.ajax({
                    type: 'POST',
                    url:"/daily"+String(gtr),
                    data: {csrfmiddlewaretoken: window.CSRF_TOKEN, Pres: Pres.value},
                    success:function(response){}});
            });
        };
    });

    inputValueK.addEventListener("input", function () {
        if (inputValueK.value >= 0.9 && inputValueK.value <= 1.1) {
            iconK.innerHTML = "&#10004;"; // pass icon
            iconK.style.color = "green";
        } else {
            iconK.innerHTML = "&#10008;"; // fail icon
            iconK.style.color = "red";
        }
        MiscUpdate();
        MiscCalc();
        DoseCalc ();
        KtpOut.textContent = KtpOut.value;
    });
    inputValueK.addEventListener("blur", function(){
        if (inputValueK.value >= 0.9 && inputValueK.value <= 1.1) {
            $(function() {
                $.ajax({
                    type: 'POST',
                    url:"/daily"+String(gtr),
                    data: {csrfmiddlewaretoken: window.CSRF_TOKEN, kfactor: K},
                    success:function(response){}});
            });
        }
    });
    laserX.addEventListener("change", function(){
        MiscCheck();
        laserX.value = laserX.checked;
        if (miscChecksX.length == miscChecks0.length) {
            iconMisc.innerHTML = "&#10004;"; // pass icon
            iconMisc.style.color = "green";
        } else {
            iconMisc.innerHTML = "&#10008;"; // fail icon
            iconMisc.style.color = "red";
        };
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, X: laserX.value},
                success:function(response){}});
        });
    });

    laserY.addEventListener("change", function(){
        MiscCheck();
        laserY.value = laserY.checked;
        if (miscChecksX.length == miscChecks0.length) {
            iconMisc.innerHTML = "&#10004;"; // pass icon
            iconMisc.style.color = "green";
        } else {
            iconMisc.innerHTML = "&#10008;"; // fail icon
            iconMisc.style.color = "red";
        };
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, Y: laserY.value},
                success:function(response){}});
        });
    });

    laserZ.addEventListener("change", function(){
        MiscCheck();
        laserZ.value = laserZ.checked;
        if (miscChecksX.length == miscChecks0.length) {
            iconMisc.innerHTML = "&#10004;"; // pass icon
            iconMisc.style.color = "green";
        } else {
            iconMisc.innerHTML = "&#10008;"; // fail icon
            iconMisc.style.color = "red";
        };
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, Z: laserZ.value},
                success:function(response){}});
        });
    });

    flatpanels.addEventListener("change", function(){
        MiscCheck();
        flatpanels.value = flatpanels.checked;
        if (miscChecksX.length == miscChecks0.length) {
            iconMisc.innerHTML = "&#10004;"; // pass icon
            iconMisc.style.color = "green";
        } else {
            iconMisc.innerHTML = "&#10008;"; // fail icon
            iconMisc.style.color = "red";
        };
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, FlatPanels: flatpanels.value},
                success:function(response){}});
        });
    });

    DynR.addEventListener("change", function(){
        MiscCheck();
        DynR.value = DynR.checked;
        if (miscChecksX.length == miscChecks0.length) {
            iconMisc.innerHTML = "&#10004;"; // pass icon
            iconMisc.style.color = "green";
        } else {
            iconMisc.innerHTML = "&#10008;"; // fail icon
            iconMisc.style.color = "red";
        };
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, DynR: DynR.value},
                success:function(response){}});
        });
    });

    VisionRT.addEventListener("change", function(){
        MiscCheck();
        VisionRT.value = VisionRT.checked;
        if (miscChecksX.length == miscChecks0.length) {
            iconMisc.innerHTML = "&#10004;"; // pass icon
            iconMisc.style.color = "green";
        } else {
            iconMisc.innerHTML = "&#10008;"; // fail icon
            iconMisc.style.color = "red";
        };
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, VisionRT: VisionRT.value},
                success:function(response){}});
        });
    });


    submitB.addEventListener("click", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, tlacitko: submitB.value},
                success: function(response){
                    document.location.href = "/success2";}});
        });
    });
    var tempJS
    reload.addEventListener("click", function(){
        $(function() {
            $.ajax({
            type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, reload: reload.value},
                success:function(response){}});
        });
        // fetch('http://127.0.0.1:8000/daily'+String(gtr), {
        //     headers:{
        //         'Accept': 'application/json',
        //         'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
        //         },
        //     })
        //     .then(response => {
        //         return response.json() //Convert response to JSON
        //     })
        //     .then(data => {
        //         // if data key != none, tak spravi list non none keys. for loop cez ten list na priradenie
        //         inputValueTemp.value = data['my_data']
        //         console.log(data['my_data'])
        //     })
    });

        //$(function () {
        //    $.ajax({
        //        type: 'GET',
        //        url:"/daily"+String(gtr),
        //       data: tempJS,
        //        //dataType: 'json',
        //        error:function(response){
        //            console.log('EEE')},
        //        success:function(response){
        //            console.log(tempJS)
        //        }})});


    //console.log(Pres.value);
    
    //Pres.textContent = p;
    //Temp.textContent = T;

    // lynx vars
    inputValueL11595 = document.getElementById("L115-95");
    iconL11595 = document.getElementById("iconL115-95");
    inputValueL11599 = document.getElementById("L115-99");
    iconL11599 = document.getElementById("iconL115-99");
    inputValueL14595 = document.getElementById("L145-95");
    iconL14595 = document.getElementById("iconL145-95");
    inputValueL14599 = document.getElementById("L145-99");
    iconL14599 = document.getElementById("iconL145-99");
    inputValueL22695 = document.getElementById("L226-95");
    iconL22695 = document.getElementById("iconL226-95");
    inputValueL22699 = document.getElementById("L226-99");
    iconL22699 = document.getElementById("iconL226-99");

    L115avg = document.getElementById("L115-avg");
    L115max = document.getElementById("L115-max");
    L145avg = document.getElementById("L145-avg");
    L145max = document.getElementById("L145-max");
    L226avg = document.getElementById("L226-avg");
    L226max = document.getElementById("L226-max");
    // lynx value checks
    inputValueL11595.addEventListener("input", function () {
        L11595out = inputValueL11595.value;
        if (inputValueL11595.value >= 95 && inputValueL11595.value <= 100) {
            iconL11595.innerHTML = "&#10004;"; // pass icon
            iconL11595.style.color = "green";
        } else {
            iconL11595.innerHTML = "&#10008;"; // fail icon
            iconL11595.style.color = "red";
        }
    });
    inputValueL11595.addEventListener("blur", function(){
        if (inputValueL11595.value >= 95 && inputValueL11595.value <= 100) {
            $(function() {
                $.ajax({
                    type: 'POST',
                    url:"/daily"+String(gtr),
                    data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L11595: L11595out},
                    success:function(response){}});
            });
        }
    });

    inputValueL11599.addEventListener("input", function () {
        L11599out = inputValueL11599.value;
        if (inputValueL11599.value >= 99 && inputValueL11599.value <= 100) {
            iconL11599.innerHTML = "&#10004;"; // pass icon
            iconL11599.style.color = "green";
        } else {
            iconL11599.innerHTML = "&#10008;"; // fail icon
            iconL11599.style.color = "red";
        }
    });
    inputValueL11599.addEventListener("blur", function(){
        if (inputValueL11599.value >= 99 && inputValueL11599.value <= 100) {
            $(function() {
                $.ajax({
                    type: 'POST',
                    url:"/daily"+String(gtr),
                    data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L11599: L11599out},
                    success:function(response){}});
            });
        }
    });

    L115avg.addEventListener("input", function () {
        L115avgout = L115avg.value;
    });
    L115avg.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L115avg: L115avgout},
                success:function(response){}});
        });
    });

    L115max.addEventListener("input", function () {
        L115maxout = L115max.value;
    });
    L115max.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L115max: L115maxout},
                success:function(response){}});
        });
    });

    inputValueL14595.addEventListener("input", function () {
        L14595out = inputValueL14595.value;
        if (inputValueL14595.value >= 95 && inputValueL14595.value <= 100) {
            iconL14595.innerHTML = "&#10004;"; // pass icon
            iconL14595.style.color = "green";
        } else {
            iconL14595.innerHTML = "&#10008;"; // fail icon
            iconL14595.style.color = "red";
        }
    });
    inputValueL14595.addEventListener("blur", function(){
        if (inputValueL14595.value >= 95 && inputValueL14595.value <= 100) {
            $(function() {
                $.ajax({
                    type: 'POST',
                    url:"/daily"+String(gtr),
                    data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L14595: L14595out},
                    success:function(response){}});
            });
        };
    });

    inputValueL14599.addEventListener("input", function () {
        L14599out = inputValueL14599.value;
        if (inputValueL14599.value >= 99 && inputValueL14599.value <= 100) {
            iconL14599.innerHTML = "&#10004;"; // pass icon
            iconL14599.style.color = "green";
        } else {
            iconL14599.innerHTML = "&#10008;"; // fail icon
            iconL14599.style.color = "red";
        }
    });
    inputValueL14599.addEventListener("blur", function(){
        if (inputValueL14599.value >= 99 && inputValueL14599.value <= 100) {
            $(function() {
                $.ajax({
                    type: 'POST',
                    url:"/daily"+String(gtr),
                    data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L14599: L14599out},
                    success:function(response){}});
            });
        }
    });

    L145avg.addEventListener("input", function () {
        L145avgout = L145avg.value;
    });
    L145avg.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L145avg: L145avgout},
                success:function(response){}});
        });
    });

    L145max.addEventListener("input", function () {
        L145maxout = L145max.value;
    });
    L145max.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L145max: L145maxout},
                success:function(response){}});
        });
    });

    inputValueL22695.addEventListener("input", function () {
        L22695out = inputValueL22695.value;
        if (inputValueL22695.value >= 95 && inputValueL22695.value <= 100) {
            iconL22695.innerHTML = "&#10004;"; // pass icon
            iconL22695.style.color = "green";
        } else {
            iconL22695.innerHTML = "&#10008;"; // fail icon
            iconL22695.style.color = "red";
        }
    });
    inputValueL22695.addEventListener("blur", function(){
        if (inputValueL22695.value >= 95 && inputValueL22695.value <= 100) {
            $(function() {
                $.ajax({
                    type: 'POST',
                    url:"/daily"+String(gtr),
                    data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L22695: L22695out},
                    success:function(response){}});
            });
        }
    });

    inputValueL22699.addEventListener("input", function () {
        L22699out = inputValueL22699.value;
        if (inputValueL22699.value >= 99 && inputValueL22699.value <= 100) {
            iconL22699.innerHTML = "&#10004;"; // pass icon
            iconL22699.style.color = "green";
        } else {
            iconL22699.innerHTML = "&#10008;"; // fail icon
            iconL22699.style.color = "red";
        }
    });
    inputValueL22699.addEventListener("blur", function(){
        if (inputValueL22699.value >= 99 && inputValueL22699.value <= 100) {
            $(function() {
                $.ajax({
                    type: 'POST',
                    url:"/daily"+String(gtr),
                    data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L22699: L22699out},
                    success:function(response){}});
            });
        }
    });
    
    L226avg.addEventListener("input", function () {
        L226avgout = L226avg.value;
    });
    L226avg.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L226avg: L226avgout},
                success:function(response){}});
        });
    });

    L226max.addEventListener("input", function () {
        L226maxout = L226max.value;
    });
    L226max.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L226max: L226maxout},
                success:function(response){}});
        });
    });

    //komora
    komoraSelect.addEventListener("change", function () {
        MiscUpdate();
        MiscCalc();
        DoseCalc();
        if (komoraSelect.value == "none"){
            KpolOut.textContent = "";
            KsatOut.textContent = "";
            KqqOut.textContent = "";
        } else if (komoraSelect.value == "3190") {
            KpolOut.textContent = K3190Kpol;
            KsatOut.textContent = K3190Ksat;
            KqqOut.textContent = Kqq;
            KpolOut.value = K3190Kpol;
            KsatOut.value = K3190Ksat;
            KqqOut.value = Kqq;
            NDW = K3190ndw;
            DoseCalc();
        } else if (komoraSelect.value == "2132") {
            KpolOut.textContent = K2132Kpol;
            KsatOut.textContent = K2132Ksat;
            KqqOut.textContent = Kqq;
            KpolOut.value = K2132Kpol;
            KsatOut.value = K2132Ksat;
            KqqOut.value = Kqq;
            NDW = K2132ndw;
            DoseCalc();
        } else if (komoraSelect.value == "3565") {
            KpolOut.textContent = K3565Kpol;
            KsatOut.textContent = K3565Ksat;
            KqqOut.textContent = Kqq;
            KpolOut.value = K3565Kpol;
            KsatOut.value = K3565Ksat;
            KqqOut.value = Kqq;
            NDW = K3565ndw;
            DoseCalc();
        } else if (komoraSelect.value == "4218") {
            KpolOut.textContent = K4218Kpol;
            KsatOut.textContent = K4218Ksat;
            KqqOut.textContent = Kqq;
            KpolOut.value = K4218Kpol;
            KsatOut.value = K4218Ksat;
            KqqOut.value = Kqq;
            NDW = K4218ndw;
            DoseCalc();
        } else if (komoraSelect.value == "5414") {
            KpolOut.textContent = K5414Kpol;
            KsatOut.textContent = K5414Ksat;
            KqqOut.textContent = Kqq;
            KpolOut.value = K5414Kpol;
            KsatOut.value = K5414Ksat;
            KqqOut.value = Kqq;
            NDW = K5414ndw;
            DoseCalc();
        }
    });
    // komora vars
    inputValueK100nC = document.getElementById("K100-nC");
    inputValueK100mu = document.getElementById("K100-mu");
    iconK100 = document.getElementById("iconK100");
    inputValueK170nC = document.getElementById("K170-nC");
    inputValueK170mu = document.getElementById("K170-mu");
    iconK170 = document.getElementById("iconK170");
    inputValueK226nC = document.getElementById("K226-nC");
    inputValueK226mu = document.getElementById("K226-mu");
    iconK226 = document.getElementById("iconK226");
    // calculations komora
    K100outD = document.getElementById('K100outD');
    K100out = document.getElementById('K100out');
    K170outD = document.getElementById('K170outD');
    K170out = document.getElementById('K170out');
    K226outD = document.getElementById('K226outD');
    K226out = document.getElementById('K226out');

    inputValueK100mu.addEventListener("input", function () {
        K100mu = inputValueK100mu.value;
        MiscUpdate();
        MiscCalc();
        DoseCalc();
    });
    inputValueK100mu.addEventListener("blur", function () {
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, K100mu: K100mu},
                success:function(response){}});
        });
    });
    inputValueK100nC.addEventListener("input", function () {
        K100nc = inputValueK100nC.value;
        MiscUpdate();
        MiscCalc();
        DoseCalc();
    });
    inputValueK100nC.addEventListener("blur", function () {
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, K100nc: K100nc},
                success:function(response){}});
        });
    });

    inputValueK170mu.addEventListener("input", function () {
        K170mu = inputValueK170mu.value;
        MiscUpdate();
        MiscCalc();
        DoseCalc();
    });
    inputValueK170mu.addEventListener("blur", function () {
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, K170mu: K170mu},
                success:function(response){}});
        });
    });
    inputValueK170nC.addEventListener("input", function () {
        K170nc = inputValueK170nC.value;
        MiscUpdate();
        MiscCalc();
        DoseCalc();
        if (dev170 >= -2 && dev170 <= 2) {
            iconK170.innerHTML = "&#10004;"; // pass icon
            iconK170.style.color = "green";
        } else {
            iconK170.innerHTML = "&#10008;"; // fail icon
            iconK170.style.color = "red";
        };
    });
    inputValueK170nC.addEventListener("blur", function () {
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, K170nc: K170nc},
                success:function(response){}});
        });
    });

    inputValueK226mu.addEventListener("input", function () {
        K226mu = inputValueK226mu.value;
        MiscUpdate();
        MiscCalc();
        DoseCalc();
    });
    inputValueK226mu.addEventListener("blur", function () {
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, K226mu: K226mu},
                success:function(response){}});
        });
    });
    inputValueK226nC.addEventListener("input", function () {
        K226nc = inputValueK226nC.value;
        MiscUpdate();
        MiscCalc();
        DoseCalc();
        if (dev226 >= -2 && dev226 <= 2) {
            iconK226.innerHTML = "&#10004;"; // pass icon
            iconK226.style.color = "green";
        } else {
            iconK226.innerHTML = "&#10008;"; // fail icon
            iconK226.style.color = "red";
        };
    });
    inputValueK226nC.addEventListener("blur", function () {
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, K226nc: K226nc},
                success:function(response){}});
        });
    });
    
    // mlic vars
    MLIC100 = document.getElementById("MLIC100");
    MLIC170 = document.getElementById("MLIC170");
    MLIC226 = document.getElementById("MLIC226");

    iconMLIC100 = document.getElementById("iconMLIC100");
    iconMLIC170 = document.getElementById("iconMLIC170");
    iconMLIC226 = document.getElementById("iconMLIC226");

    MLIC100out = document.getElementById("MLIC100out");
    MLIC170out = document.getElementById("MLIC170out");
    MLIC226out = document.getElementById("MLIC226out");

    //mlic calcs
    MLIC100.addEventListener("input", function () {
        MLIC100out.value = MLIC100.value;
        MiscUpdate();
        MiscCalc();
        MlicCalc();
    });
    MLIC100.addEventListener("blur", function () {
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, MLIC100: MLIC100out.value},
                success:function(response){}});
        });
    });

    MLIC170.addEventListener("input", function () {
        MLIC170out.value = MLIC170.value;
        MiscUpdate();
        MiscCalc();
        MlicCalc();
    });
    MLIC170.addEventListener("blur", function () {
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, MLIC170: MLIC170out.value},
                success:function(response){}});
        });
    });

    MLIC226.addEventListener("input", function () {
        MLIC226out.value = MLIC226.value;
        MiscUpdate();
        MiscCalc();
        MlicCalc();
    });
    MLIC226.addEventListener("blur", function () {
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily"+String(gtr),
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, MLIC226: MLIC226out.value},
                success:function(response){}});
        });
    });


    //var datacheck = json.parse("{{ datacheck }}");
    //alert(datacheck);
    

    //function updateState() {
    //    let allChecked = true;
    //    for (let i = 0; i < checkboxes.length; i++) {
    //        const checkbox = checkboxes[i];

    //        // Skip checkboxes inside a hidden parent element
    //        if (checkbox.offsetParent === null) {
    //            continue;
    //        }

    //        if (!checkbox.checked) {
    //            allChecked = false;
    //            break;
    //        }
    //    }

    //    state.allChecked = allChecked;

    //    let allGreen = true;

    //    for (let i = 0; i < checkIcons.length; i++) {
    //        const checkIcon = checkIcons[i];

    //        // Skip check icons inside a hidden parent element
    //        if (checkIcon.offsetParent === null) {
    //            continue;
    //        }

    //        if (checkIcon.style.color !== 'green') {
    //            allGreen = false;
    //            break;
    //        }
    //    }

    //    state.allGreen = allGreen;
    //    console.log(state);
    //}
    //for (let i = 0; i < checkIcons.length; i++) {
    //    checkboxes[i].addEventListener('click', updateState);
    //    const checkIcon = checkIcons[i];
    //    checkIcon.addEventListener('click', () => {
    //        if (checkIcon.style.color === 'green') {
    //            checkIcon.style.color = 'black';
    //        } else {
    //            checkIcon.style.color = 'green';
    //        }
    //        updateState();
    //    });
    //}
    //updateState();
    //if (state.allChecked = true) {
    //    iconMisc.innerHTML = "&#10004;"; // pass icon
    //    iconMisc.style.color = "green";
    //} else {
    //    iconMisc.innerHTML = "&#10008;"; // fail icon
    //    iconMisc.style.color = "red";
    //}
    //if (state.allGreen = true) {
    //    iconAll.innerHTML = "&#10004;"; // pass icon
    //    iconAll.style.color = "green";
    //} else {
    //    iconAll.innerHTML = "&#10008;"; // fail icon
    //    iconAll.style.color = "red";
    //}
});