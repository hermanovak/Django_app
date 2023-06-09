//db
// Construct the data object with your variables
document.addEventListener('DOMContentLoaded', function () {
    const lynxSelect = document.getElementById("lynx-select");
    const lynx = document.getElementById("lynx");
    const lynxLR = document.getElementById("lynxLR");

    const komoraSelect = document.getElementById("komora-select");
    const komora = document.getElementById("komora");
    const komoraLR = document.getElementById("komoraLR");

    const mlicSelect = document.getElementById("mlic-select");
    const mlic = document.getElementById("mlic");
    const mlicLR = document.getElementById("mlicLR");
    lynxSelect.addEventListener("change", function() {
        // Show the selected option form
        if (lynxSelect.value === "none") {
            lynxLR.style.display = "none";
        } else if (lynxSelect.value != "none") {
            lynxLR.style.display = "block";
        }
    });
    komoraSelect.addEventListener("change", function() {
        // Show the selected option form
        if (komoraSelect.value === "none") {
            komoraLR.style.display = "none";
        } else if (komoraSelect.value != "none") {
            komoraLR.style.display = "block";
        }
    });
    mlicSelect.addEventListener("change", function() {
        // Show the selected option form
        if (mlicSelect.value === "none") {
            mlicLR.style.display = "none";
        } else if (lynxSelect.value != "none") {
            mlicLR.style.display = "block";
        }
    });

    var data = {
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
    var inputValueL7095;
    var iconL7095;
    var inputValueL7099;
    var iconL7099;
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
    var L70avg;
    var L70max;
    var L115avg;
    var L115max;
    var L145avg;
    var L145max;
    var L226avg;
    var L226max;
    //lynx outs
    var L7095out;
    var L7099out;
    var L70avgout;
    var L70maxout;
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
    // //dose refs
    // var K70ref;
    // var K100ref;
    // var K170ref;
    // var K226ref;
    //komora outs
    var K70outD;
    var K70out;
    var K100outD;
    var K100out;
    var K170outD;
    var K170out;
    var K226outD;
    var K226out;
    //komora calcs
    var D70;
    var dev70;
    var D100;
    var dev100;
    var D170;
    var dev170;
    var D226;
    var dev226;
    //mlic vars declare
    var MLIC70;
    var MLIC100;
    var MLIC170;
    var MLIC226;
    var iconMLIC70;
    var iconMLIC100;
    var iconMLIC170;
    var iconMLIC226;
    // //mlic refs
    // var MLIC70ref;
    // var MLIC100ref;
    // var MLIC170ref;
    // var MLIC226ref;
    //mlic outs
    var MLIC70out;
    var MLIC100out;
    var MLIC170out;
    var MLIC226out;
    //mlic calcs
    var MLICdev70;
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
        Ktp = (((parseInt(Temp.value) + 273.15) / (273.15 + 20)) * (1013 / parseInt(Pres.value)));
        KtpOut.value = Ktp;
    };
    function MiscCheck () {
        miscChecksX = document.querySelectorAll('input[type="checkbox"]:checked');
    };


    //checkboxes check + check of all checks, czechs number one

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

    iconMisc = document.getElementById("icon-misc");
       
    Temp = document.getElementById("tempOut");
    Pres = document.getElementById("presOut");

    KtpOut = document.getElementById("ktpOut");

    KpolOut = document.getElementById("kpolOut");
    KsatOut = document.getElementById("ksatOut");
    KqqOut = document.getElementById("kqqOut");

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
            var T = parseInt(inputValueTemp.value) + 273.15;
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
        KtpOut.textContent = KtpOut.value;
        });
    inputValueTemp.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, Temp: Temp.value},
                success:function(response){}});
        });
    });

    inputValuePres.addEventListener("input", function () {
        if (inputValuePres.value >= 900 && inputValuePres.value <= 1100) {
            iconPres.innerHTML = "&#10004;"; // pass icon
            iconPres.style.color = "green";
            var p = parseInt(inputValuePres.value);
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
        KtpOut.textContent = KtpOut.value;
        //p = inputValuePres.value;
    });
    inputValuePres.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, Pres: Pres.value},
                success:function(response){}});
        });
    });

    inputValueK.addEventListener("input", function () {
        if (inputValueK.value >= 1 && inputValueK.value <= 1.1) {
            iconK.innerHTML = "&#10004;"; // pass icon
            iconK.style.color = "green";
        } else {
            iconK.innerHTML = "&#10008;"; // fail icon
            iconK.style.color = "red";
        }
        MiscUpdate();
        MiscCalc();
        KtpOut.textContent = KtpOut.value;
    });
    inputValueK.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, kfactor: K},
                success:function(response){}});
        });
    });

    laserX.addEventListener("input", function(){
        MiscCheck();
        if (miscChecksX.length == miscChecks0.length) {
            iconMisc.innerHTML = "&#10004;"; // pass icon
            iconMisc.style.color = "green";
        } else {
            iconMisc.innerHTML = "&#10008;"; // fail icon
            iconMisc.style.color = "red";
        };
    });
    laserX.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, X: laserX.value},
                success:function(response){}});
        });
    });

    laserY.addEventListener("input", function(){
        MiscCheck();
        if (miscChecksX.length == miscChecks0.length) {
            iconMisc.innerHTML = "&#10004;"; // pass icon
            iconMisc.style.color = "green";
        } else {
            iconMisc.innerHTML = "&#10008;"; // fail icon
            iconMisc.style.color = "red";
        };
    });
    laserY.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, Y: laserY.value},
                success:function(response){}});
        });
    });

    laserZ.addEventListener("input", function(){
        MiscCheck();
        if (miscChecksX.length == miscChecks0.length) {
            iconMisc.innerHTML = "&#10004;"; // pass icon
            iconMisc.style.color = "green";
        } else {
            iconMisc.innerHTML = "&#10008;"; // fail icon
            iconMisc.style.color = "red";
        };
    });
    laserZ.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, Z: laserZ.value},
                success:function(response){}});
        });
    });

    flatpanels.addEventListener("input", function(){
        MiscCheck();
        if (miscChecksX.length == miscChecks0.length) {
            iconMisc.innerHTML = "&#10004;"; // pass icon
            iconMisc.style.color = "green";
        } else {
            iconMisc.innerHTML = "&#10008;"; // fail icon
            iconMisc.style.color = "red";
        };
    });
    flatpanels.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, FlatPanels: flatpanels.value},
                success:function(response){}});
        });
    });

    DynR.addEventListener("input", function(){
        MiscCheck();
        if (miscChecksX.length == miscChecks0.length) {
            iconMisc.innerHTML = "&#10004;"; // pass icon
            iconMisc.style.color = "green";
        } else {
            iconMisc.innerHTML = "&#10008;"; // fail icon
            iconMisc.style.color = "red";
        };
    });
    DynR.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, DynR: DynR.value},
                success:function(response){}});
        });
    });

    VisionRT.addEventListener("input", function(){
        MiscCheck();
        if (miscChecksX.length == miscChecks0.length) {
            iconMisc.innerHTML = "&#10004;"; // pass icon
            iconMisc.style.color = "green";
        } else {
            iconMisc.innerHTML = "&#10008;"; // fail icon
            iconMisc.style.color = "red";
        };
    });
    VisionRT.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, VisionRT: VisionRT.value},
                success:function(response){}});
        });
    });


    
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
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L11595: L11595out},
                success:function(response){}});
        });
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
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L11599: L11599out},
                success:function(response){}});
        });
    });

    L115avg.addEventListener("input", function () {
        L115avgout = L115avg.value;
    });
    L115avg.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
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
                url:"/daily",
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
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L14595: L14595out},
                success:function(response){}});
        });
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
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L14599: L14599out},
                success:function(response){}});
        });
    });

    L145avg.addEventListener("input", function () {
        L145avgout = L145avg.value;
    });
    L145avg.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
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
                url:"/daily",
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
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L22695: L22695out},
                success:function(response){}});
        });
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
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L22699: L22699out},
                success:function(response){}});
        });
    });
    
    L226avg.addEventListener("input", function () {
        L226avgout = L226avg.value;
    });
    L226avg.addEventListener("blur", function(){
        $(function() {
            $.ajax({
                type: 'POST',
                url:"/daily",
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
                url:"/daily",
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN, L226max: L226maxout},
                success:function(response){}});
        });
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
    komoraSelect.addEventListener("change", function () {
    if (komoraSelect.value === "komora3190") {
        inputValueK100mu.addEventListener("input", function () {
            D100 = inputValueK100nC.value * 100 / inputValueK100mu.value * K3190ndw * KtpOut * K3190Ksat * K3190Kpol * Kqq;
            K100outD.textContent = D100;
            dev100 = ((D100 / K100ref) - 1) * 100;
            K100out.textContent = dev100;
            if (dev100 >= -2 && dev100 <= 2) {
                iconK100.innerHTML = "&#10004;"; // pass icon
                iconK100.style.color = "green";
            } else {
                iconK100.innerHTML = "&#10008;"; // fail icon
                iconK100.style.color = "red";
            };
        });
        inputValueK170mu.addEventListener("input", function () {
            D170 = inputValueK170nC.value * 100 / inputValueK170mu.value * K3190ndw * KtpOut * K3190Ksat * K3190Kpol * Kqq;
            K170outD.textContent = D170;
            dev170 = ((D170 / K170ref) - 1) * 100;
            K170out.textContent = dev170;
            if (dev170 >= -2 && dev170 <= 2) {
                iconK170.innerHTML = "&#10004;"; // pass icon
                iconK170.style.color = "green";
            } else {
                iconK170.innerHTML = "&#10008;"; // fail icon
                iconK170.style.color = "red";
            };
        });
        inputValueK226mu.addEventListener("input", function () {
            D226 = inputValueK226nC.value * 100 / inputValueK226mu.value * K3190ndw * KtpOut * K3190Ksat * K3190Kpol * Kqq;
            K226outD.textContent = D226;
            dev226 = ((D226 / K226ref) - 1) * 100;
            K226out.textContent = dev226;
            if (dev226 >= -2 && dev226 <= 2) {
                iconK226.innerHTML = "&#10004;"; // pass icon
                iconK226.style.color = "green";
            } else {
                iconK226.innerHTML = "&#10008;"; // fail icon
                iconK226.style.color = "red";
            };
        });
        KpolOut.textContent = K3190Kpol;
        KsatOut.textContent = K3190Ksat;
        KqqOut.textContent = Kqq;
    } else if (komoraSelect.value === "komora2132") {
        inputValueK100mu.addEventListener("input", function () {
            D100 = inputValueK100nC.value * 100 / inputValueK100mu.value * K2132ndw * KtpOut * K2132Ksat * K2132Kpol * Kqq;
            K100outD.textContent = D100;
            dev100 = ((D100 / K100ref) - 1) * 100;
            K100out.textContent = dev100;
            if (dev100 >= -2 && dev100 <= 2) {
                iconK100.innerHTML = "&#10004;"; // pass icon
                iconK100.style.color = "green";
            } else {
                iconK100.innerHTML = "&#10008;"; // fail icon
                iconK100.style.color = "red";
            };
        });
        inputValueK170mu.addEventListener("input", function () {
            D170 = inputValueK170nC.value * 100 / inputValueK170mu.value * K2132ndw * KtpOut * K2132Ksat * K2132Kpol * Kqq;
            K170outD.textContent = D170;
            dev170 = ((D170 / K170ref) - 1) * 100;
            K170out.textContent = dev170;
            if (dev170 >= -2 && dev170 <= 2) {
                iconK170.innerHTML = "&#10004;"; // pass icon
                iconK170.style.color = "green";
            } else {
                iconK170.innerHTML = "&#10008;"; // fail icon
                iconK170.style.color = "red";
            };
        });
        inputValueK226mu.addEventListener("input", function () {
            D226 = inputValueK226nC.value * 100 / inputValueK226mu.value * K2132ndw * KtpOut * K2132Ksat * K2132Kpol * Kqq;
            K226outD.textContent = D226;
            dev226 = ((D226 / K226ref) - 1) * 100;
            K226out.textContent = dev226;
            if (dev226 >= -2 && dev226 <= 2) {
                iconK226.innerHTML = "&#10004;"; // pass icon
                iconK226.style.color = "green";
            } else {
                iconK226.innerHTML = "&#10008;"; // fail icon
                iconK226.style.color = "red";
            };
        });
        KpolOut.textContent = K2132Kpol;
        KsatOut.textContent = K2132Ksat;
        KqqOut.textContent = Kqq;
    } else if (komoraSelect.value === "komora3565") {
        inputValueK100mu.addEventListener("input", function () {
            D100 = inputValueK100nC.value * 100 / inputValueK100mu.value * K3565ndw * KtpOut * K3565Ksat * K3565Kpol * Kqq;
            K100outD.textContent = D100;
            dev100 = ((D100 / K100ref) - 1) * 100;
            K100out.textContent = dev100;
            if (dev100 >= -2 && dev100 <= 2) {
                iconK100.innerHTML = "&#10004;"; // pass icon
                iconK100.style.color = "green";
            } else {
                iconK100.innerHTML = "&#10008;"; // fail icon
                iconK100.style.color = "red";
            };
        });
        inputValueK170mu.addEventListener("input", function () {
            D170 = inputValueK170nC.value * 100 / inputValueK170mu.value * K3565ndw * KtpOut * K3565Ksat * K3565Kpol * Kqq;
            K170outD.textContent = D170;
            dev170 = ((D170 / K170ref) - 1) * 100;
            K170out.textContent = dev170;
            if (dev170 >= -2 && dev170 <= 2) {
                iconK170.innerHTML = "&#10004;"; // pass icon
                iconK170.style.color = "green";
            } else {
                iconK170.innerHTML = "&#10008;"; // fail icon
                iconK170.style.color = "red";
            };
        });
        inputValueK226mu.addEventListener("input", function () {
            D226 = inputValueK226nC.value * 100 / inputValueK226mu.value * K3565ndw * KtpOut * K3565Ksat * K3565Kpol * Kqq;
            K226outD.textContent = D226;
            dev226 = ((D226 / K226ref) - 1) * 100;
            K226out.textContent = dev226;
            if (dev226 >= -2 && dev226 <= 2) {
                iconK226.innerHTML = "&#10004;"; // pass icon
                iconK226.style.color = "green";
            } else {
                iconK226.innerHTML = "&#10008;"; // fail icon
                iconK226.style.color = "red";
            };
        });
        KpolOut.textContent = K3565Kpol;
        KsatOut.textContent = K3565Ksat;
        KqqOut.textContent = Kqq;
    } else if (komoraSelect.value === "komora4218") {
        inputValueK100mu.addEventListener("input", function () {
            D100 = inputValueK100nC.value * 100 / inputValueK100mu.value * K4218ndw * KtpOut * K4218Ksat * K4218Kpol * Kqq;
            K100outD.textContent = D100;
            dev100 = ((D100 / K100ref) - 1) * 100;
            K100out.textContent = dev100;
            if (dev100 >= -2 && dev100 <= 2) {
                iconK100.innerHTML = "&#10004;"; // pass icon
                iconK100.style.color = "green";
            } else {
                iconK100.innerHTML = "&#10008;"; // fail icon
                iconK100.style.color = "red";
            };
        });
        inputValueK170mu.addEventListener("input", function () {
            D170 = inputValueK170nC.value * 100 / inputValueK170mu.value * K4218ndw * KtpOut * K4218Ksat * K4218Kpol * Kqq;
            K170outD.textContent = D170;
            dev170 = ((D170 / K170ref) - 1) * 100;
            K170out.textContent = dev170;
            if (dev170 >= -2 && dev170 <= 2) {
                iconK170.innerHTML = "&#10004;"; // pass icon
                iconK170.style.color = "green";
            } else {
                iconK170.innerHTML = "&#10008;"; // fail icon
                iconK170.style.color = "red";
            };
        });
        inputValueK226mu.addEventListener("input", function () {
            D226 = inputValueK226nC.value * 100 / inputValueK226mu.value * K4218ndw * KtpOut * K4218Ksat * K4218Kpol * Kqq;
            K226outD.textContent = D226;
            dev226 = ((D226 / K226ref) - 1) * 100;
            K226out.textContent = dev226;
            if (dev226 >= -2 && dev226 <= 2) {
                iconK226.innerHTML = "&#10004;"; // pass icon
                iconK226.style.color = "green";
            } else {
                iconK226.innerHTML = "&#10008;"; // fail icon
                iconK226.style.color = "red";
            };
        });
        KpolOut.textContent = K4218Kpol;
        KsatOut.textContent = K4218Ksat;
        KqqOut.textContent = Kqq;
    } else if (komoraSelect.value === "komora5414") {
        inputValueK100mu.addEventListener("input", function () {
            D100 = inputValueK100nC.value * 100 / inputValueK100mu.value * K5414ndw * KtpOut * K5414Ksat * K5414Kpol * Kqq;
            K100outD.textContent = D100;
            dev100 = ((D100 / K100ref) - 1) * 100;
            K100out.textContent = dev100;
            if (dev100 >= -2 && dev100 <= 2) {
                iconK100.innerHTML = "&#10004;"; // pass icon
                iconK100.style.color = "green";
            } else {
                iconK100.innerHTML = "&#10008;"; // fail icon
                iconK100.style.color = "red";
            };
        });
        inputValueK170mu.addEventListener("input", function () {
            D170 = inputValueK170nC.value * 100 / inputValueK170mu.value * K5414ndw * KtpOut * K5414Ksat * K5414Kpol * Kqq;
            K170outD.textContent = D170;
            dev170 = ((D170 / K170ref) - 1) * 100;
            K170out.textContent = dev170;
            if (dev170 >= -2 && dev170 <= 2) {
                iconK170.innerHTML = "&#10004;"; // pass icon
                iconK170.style.color = "green";
            } else {
                iconK170.innerHTML = "&#10008;"; // fail icon
                iconK170.style.color = "red";
            };
        });
        inputValueK226mu.addEventListener("input", function () {
            D226 = inputValueK226nC.value * 100 / inputValueK226mu.value * K5414ndw * KtpOut * K5414Ksat * K5414Kpol * Kqq;
            K226outD.textContent = D226;
            dev226 = ((D226 / K226ref) - 1) * 100;
            K226out.textContent = dev226;
            if (dev226 >= -2 && dev226 <= 2) {
                iconK226.innerHTML = "&#10004;"; // pass icon
                iconK226.style.color = "green";
            } else {
                iconK226.innerHTML = "&#10008;"; // fail icon
                iconK226.style.color = "red";
            };
        });
        KpolOut.textContent = K5414Kpol;
        KsatOut.textContent = K5414Ksat;
        KqqOut.textContent = Kqq;
        }
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
    mlicSelect.addEventListener("change", function () {
        if (mlicSelect.value === "mlic1") {
            MLIC100.addEventListener("input", function () {
                MLICdev100 = MLIC100.value - MLIC100ref;
                MLIC100out.value = MLIC100.value;
                MLIC100out.textContent = MLICdev100;
                if (MLICdev100 >= -0.15 && MLICdev100 <= 0.15) {
                    iconMLIC100.innerHTML = "&#10004;"; // pass icon
                    iconMLIC100.style.color = "green";
                } else {
                    iconMLIC100.innerHTML = "&#10008;"; // fail icon
                    iconMLIC100.style.color = "red";
                };
            });
            MLIC170.addEventListener("input", function () {
                MLICdev170 = MLIC170.value - MLIC170ref;
                MLIC170out.value = MLIC170.value;
                MLIC170out.textContent = MLICdev170;
                if (MLICdev170 >= -0.15 && MLICdev170 <= 0.15) {
                    iconMLIC170.innerHTML = "&#10004;"; // pass icon
                    iconMLIC170.style.color = "green";
                } else {
                    iconMLIC170.innerHTML = "&#10008;"; // fail icon
                    iconMLIC170.style.color = "red";
                };
            });
            MLIC226.addEventListener("input", function () {
                MLICdev226 = MLIC226.value - MLIC226ref;
                MLIC226out.value = MLIC226.value;
                MLIC226out.textContent = MLICdev226;
                if (MLICdev226 >= -0.15 && MLICdev226 <= 0.15) {
                    iconMLIC226.innerHTML = "&#10004;"; // pass icon
                    iconMLIC226.style.color = "green";
                } else {
                    iconMLIC226.innerHTML = "&#10008;"; // fail icon
                    iconMLIC226.style.color = "red";
                };
            });
        }
    });
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