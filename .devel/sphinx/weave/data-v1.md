





(sec:data-v1)=
# Explore Datasets (v1.1.0)





*Select battery/dataset from the {ref}`sec:suite-v1`:*

::::{raw} html
<form style="margin-bottom: 2em">

<div style="text-align: center">
<span id="select_prev" class="btn btn-neutral float-left" title="Previous dataset"><span class="fa fa-arrow-circle-left" aria-hidden="true"></span></span>

<select id="select_battery" name="select_battery" class="btn btn-neutral">
</select>
/
<select id="select_dataset" name="select_dataset" class="btn btn-neutral">
</select>

<span id="select_next" class="btn btn-neutral float-right" title="Next dataset"><span class="fa fa-arrow-circle-right" aria-hidden="true"></span></span>
</div>

</form>
::::


*Preview (only for 1–3 dimensional datasets):*

::::{raw} html

<div id="dataset_showcase">

</div>
::::




::::{raw} html
<script type="text/javascript">

var suite =
{"wut": {"circles": ["labels0"], "cross": ["labels0"], "graph": ["labels0"], "isolation": ["labels0"], "labirynth": ["labels0"], "mk1": ["labels0"], "mk2": ["labels0"], "mk3": ["labels0"], "mk4": ["labels0"], "olympic": ["labels0"], "smile": ["labels0", "labels1"], "stripes": ["labels0"], "trajectories": ["labels0"], "trapped_lovers": ["labels0"], "twosplashes": ["labels0"], "windows": ["labels0"], "x1": ["labels0"], "x2": ["labels0", "labels1"], "x3": ["labels0", "labels1"], "z1": ["labels0"], "z2": ["labels0"], "z3": ["labels0"]}, "sipu": {"a1": ["labels0"], "a2": ["labels0"], "a3": ["labels0"], "aggregation": ["labels0"], "birch1": ["labels0"], "birch2": ["labels0"], "compound": ["labels0", "labels1", "labels2", "labels3", "labels4"], "d31": ["labels0"], "flame": ["labels0", "labels1"], "jain": ["labels0"], "pathbased": ["labels0", "labels1"], "r15": ["labels0", "labels1", "labels2"], "s1": ["labels0"], "s2": ["labels0"], "s3": ["labels0"], "s4": ["labels0"], "spiral": ["labels0"], "unbalance": ["labels0"], "worms_2": ["labels0"], "worms_64": ["labels0"]}, "fcps": {"atom": ["labels0"], "chainlink": ["labels0"], "engytime": ["labels0", "labels1"], "hepta": ["labels0"], "lsun": ["labels0"], "target": ["labels0", "labels1"], "tetra": ["labels0"], "twodiamonds": ["labels0"], "wingnut": ["labels0"]}, "graves": {"dense": ["labels0"], "fuzzyx": ["labels0", "labels1", "labels2", "labels3", "labels4"], "line": ["labels0"], "parabolic": ["labels0", "labels1"], "ring": ["labels0"], "ring_noisy": ["labels0"], "ring_outliers": ["labels0", "labels1"], "zigzag": ["labels0", "labels1"], "zigzag_noisy": ["labels0", "labels1"], "zigzag_outliers": ["labels0", "labels1"]}, "other": {"chameleon_t4_8k": ["labels0"], "chameleon_t5_8k": ["labels0"], "chameleon_t7_10k": ["labels0"], "chameleon_t8_8k": ["labels0"], "hdbscan": ["labels0"], "iris": ["labels0"], "iris5": ["labels0"], "square": ["labels0"]}, "uci": {"ecoli": ["labels0"], "glass": ["labels0"], "ionosphere": ["labels0"], "sonar": ["labels0"], "statlog": ["labels0"], "wdbc": ["labels0"], "wine": ["labels0"], "yeast": ["labels0"]}, "mnist": {"digits": ["labels0"], "fashion": ["labels0"]}, "g2mg": {"g2mg_1_10": ["labels0", "labels1"], "g2mg_1_20": ["labels0", "labels1"], "g2mg_1_30": ["labels0", "labels1"], "g2mg_1_40": ["labels0", "labels1"], "g2mg_1_50": ["labels0", "labels1"], "g2mg_1_60": ["labels0", "labels1"], "g2mg_1_70": ["labels0", "labels1"], "g2mg_1_80": ["labels0", "labels1"], "g2mg_1_90": ["labels0", "labels1"], "g2mg_2_10": ["labels0", "labels1"], "g2mg_2_20": ["labels0", "labels1"], "g2mg_2_30": ["labels0", "labels1"], "g2mg_2_40": ["labels0", "labels1"], "g2mg_2_50": ["labels0", "labels1"], "g2mg_2_60": ["labels0", "labels1"], "g2mg_2_70": ["labels0", "labels1"], "g2mg_2_80": ["labels0", "labels1"], "g2mg_2_90": ["labels0", "labels1"], "g2mg_4_10": ["labels0", "labels1"], "g2mg_4_20": ["labels0", "labels1"], "g2mg_4_30": ["labels0", "labels1"], "g2mg_4_40": ["labels0", "labels1"], "g2mg_4_50": ["labels0", "labels1"], "g2mg_4_60": ["labels0", "labels1"], "g2mg_4_70": ["labels0", "labels1"], "g2mg_4_80": ["labels0", "labels1"], "g2mg_4_90": ["labels0", "labels1"], "g2mg_8_10": ["labels0", "labels1"], "g2mg_8_20": ["labels0", "labels1"], "g2mg_8_30": ["labels0", "labels1"], "g2mg_8_40": ["labels0", "labels1"], "g2mg_8_50": ["labels0", "labels1"], "g2mg_8_60": ["labels0", "labels1"], "g2mg_8_70": ["labels0", "labels1"], "g2mg_8_80": ["labels0", "labels1"], "g2mg_8_90": ["labels0", "labels1"], "g2mg_16_10": ["labels0", "labels1"], "g2mg_16_20": ["labels0", "labels1"], "g2mg_16_30": ["labels0", "labels1"], "g2mg_16_40": ["labels0", "labels1"], "g2mg_16_50": ["labels0", "labels1"], "g2mg_16_60": ["labels0", "labels1"], "g2mg_16_70": ["labels0", "labels1"], "g2mg_16_80": ["labels0", "labels1"], "g2mg_16_90": ["labels0", "labels1"], "g2mg_32_10": ["labels0", "labels1"], "g2mg_32_20": ["labels0", "labels1"], "g2mg_32_30": ["labels0", "labels1"], "g2mg_32_40": ["labels0", "labels1"], "g2mg_32_50": ["labels0", "labels1"], "g2mg_32_60": ["labels0", "labels1"], "g2mg_32_70": ["labels0", "labels1"], "g2mg_32_80": ["labels0", "labels1"], "g2mg_32_90": ["labels0", "labels1"], "g2mg_64_10": ["labels0", "labels1"], "g2mg_64_20": ["labels0", "labels1"], "g2mg_64_30": ["labels0", "labels1"], "g2mg_64_40": ["labels0", "labels1"], "g2mg_64_50": ["labels0", "labels1"], "g2mg_64_60": ["labels0", "labels1"], "g2mg_64_70": ["labels0", "labels1"], "g2mg_64_80": ["labels0", "labels1"], "g2mg_64_90": ["labels0", "labels1"], "g2mg_128_10": ["labels0", "labels1"], "g2mg_128_20": ["labels0", "labels1"], "g2mg_128_30": ["labels0", "labels1"], "g2mg_128_40": ["labels0", "labels1"], "g2mg_128_50": ["labels0", "labels1"], "g2mg_128_60": ["labels0", "labels1"], "g2mg_128_70": ["labels0", "labels1"], "g2mg_128_80": ["labels0", "labels1"], "g2mg_128_90": ["labels0", "labels1"]}, "h2mg": {"h2mg_1_10": ["labels0", "labels1"], "h2mg_1_20": ["labels0", "labels1"], "h2mg_1_30": ["labels0", "labels1"], "h2mg_1_40": ["labels0", "labels1"], "h2mg_1_50": ["labels0", "labels1"], "h2mg_1_60": ["labels0", "labels1"], "h2mg_1_70": ["labels0", "labels1"], "h2mg_1_80": ["labels0", "labels1"], "h2mg_1_90": ["labels0", "labels1"], "h2mg_2_10": ["labels0", "labels1"], "h2mg_2_20": ["labels0", "labels1"], "h2mg_2_30": ["labels0", "labels1"], "h2mg_2_40": ["labels0", "labels1"], "h2mg_2_50": ["labels0", "labels1"], "h2mg_2_60": ["labels0", "labels1"], "h2mg_2_70": ["labels0", "labels1"], "h2mg_2_80": ["labels0", "labels1"], "h2mg_2_90": ["labels0", "labels1"], "h2mg_4_10": ["labels0", "labels1"], "h2mg_4_20": ["labels0", "labels1"], "h2mg_4_30": ["labels0", "labels1"], "h2mg_4_40": ["labels0", "labels1"], "h2mg_4_50": ["labels0", "labels1"], "h2mg_4_60": ["labels0", "labels1"], "h2mg_4_70": ["labels0", "labels1"], "h2mg_4_80": ["labels0", "labels1"], "h2mg_4_90": ["labels0", "labels1"], "h2mg_8_10": ["labels0", "labels1"], "h2mg_8_20": ["labels0", "labels1"], "h2mg_8_30": ["labels0", "labels1"], "h2mg_8_40": ["labels0", "labels1"], "h2mg_8_50": ["labels0", "labels1"], "h2mg_8_60": ["labels0", "labels1"], "h2mg_8_70": ["labels0", "labels1"], "h2mg_8_80": ["labels0", "labels1"], "h2mg_8_90": ["labels0", "labels1"], "h2mg_16_10": ["labels0", "labels1"], "h2mg_16_20": ["labels0", "labels1"], "h2mg_16_30": ["labels0", "labels1"], "h2mg_16_40": ["labels0", "labels1"], "h2mg_16_50": ["labels0", "labels1"], "h2mg_16_60": ["labels0", "labels1"], "h2mg_16_70": ["labels0", "labels1"], "h2mg_16_80": ["labels0", "labels1"], "h2mg_16_90": ["labels0", "labels1"], "h2mg_32_10": ["labels0", "labels1"], "h2mg_32_20": ["labels0", "labels1"], "h2mg_32_30": ["labels0", "labels1"], "h2mg_32_40": ["labels0", "labels1"], "h2mg_32_50": ["labels0", "labels1"], "h2mg_32_60": ["labels0", "labels1"], "h2mg_32_70": ["labels0", "labels1"], "h2mg_32_80": ["labels0", "labels1"], "h2mg_32_90": ["labels0", "labels1"], "h2mg_64_10": ["labels0", "labels1"], "h2mg_64_20": ["labels0", "labels1"], "h2mg_64_30": ["labels0", "labels1"], "h2mg_64_40": ["labels0", "labels1"], "h2mg_64_50": ["labels0", "labels1"], "h2mg_64_60": ["labels0", "labels1"], "h2mg_64_70": ["labels0", "labels1"], "h2mg_64_80": ["labels0", "labels1"], "h2mg_64_90": ["labels0", "labels1"], "h2mg_128_10": ["labels0", "labels1"], "h2mg_128_20": ["labels0", "labels1"], "h2mg_128_30": ["labels0", "labels1"], "h2mg_128_40": ["labels0", "labels1"], "h2mg_128_50": ["labels0", "labels1"], "h2mg_128_60": ["labels0", "labels1"], "h2mg_128_70": ["labels0", "labels1"], "h2mg_128_80": ["labels0", "labels1"], "h2mg_128_90": ["labels0", "labels1"]}}
;
</script>

<script type="text/javascript">
function addToSelect(select_id, elems, selected=null) {
    let select = document.getElementById(select_id);
    while (select.lastChild) select.removeChild(select.lastChild);
    for (let battery in elems) {
        let opt = document.createElement("option");
        opt.value = opt.innerHTML = battery;
        if (selected) {
            if (battery == selected) opt.selected = true;
        }
        else {
            selected = battery;
        }
        select.appendChild(opt);
    }
    return selected;
}



let battery = location.hash.substring(1, location.hash.lastIndexOf("/"));
if (!(battery && (battery in suite))) battery = null;
battery = addToSelect("select_battery", suite, battery);

let dataset = location.hash.substring(location.hash.lastIndexOf("/")+1);
if (!(dataset && (dataset in suite[battery]))) dataset = null;
dataset = addToSelect("select_dataset", suite[battery], dataset);

location.hash = battery + "/" + dataset;


function selectNextDataset() {
    let select = document.getElementById('select_dataset');
    select.selectedIndex += 1;

    if (select.selectedIndex < 0) {
        let select2 = document.getElementById('select_battery');
        select2.selectedIndex += 1;
        if (select2.selectedIndex < 0)
            select2.selectedIndex = 0;

        let battery = select2.value;
        addToSelect("select_dataset", suite[battery]);

        select.selectedIndex = 0;
    }

    datasetChanged();
}


function selectPrevDataset() {
    let select = document.getElementById('select_dataset');
    select.selectedIndex -= 1;

    if (select.selectedIndex < 0) {
        let select2 = document.getElementById('select_battery');
        select2.selectedIndex -= 1;
        if (select2.selectedIndex < 0)
            select2.selectedIndex = select2.children.length-1;

        let battery = select2.value;
        addToSelect("select_dataset", suite[battery]);

        select.selectedIndex = select.children.length-1;
    }

    datasetChanged();
}



document.getElementById("select_prev").onclick = selectPrevDataset;
document.getElementById("select_next").onclick = selectNextDataset;



function datasetChanged() {
    let battery = document.getElementById("select_battery").value;
    let dataset = document.getElementById("select_dataset").value;
    location.hash = battery + "/" + dataset;
}


function batteryChanged() {
    let battery = document.getElementById("select_battery").value;
    addToSelect("select_dataset", suite[battery]);
    datasetChanged();
}

document.getElementById("select_dataset").onchange = datasetChanged;
document.getElementById("select_battery").onchange = batteryChanged;





function locationHashChanged()
{
//     els = document.getElementsByClassName("clustbench_browsable");
//     for (let i=0; i<els.length; i++)
//         els[i].style.display = "none";
//
//     var x = location.hash.substring(1);
//     if (x == "") return;
//     el = document.getElementById(x);
//     if (!el) return;
//     el.style.display = "block";

    var battery = location.hash.substring(1, location.hash.lastIndexOf("/"));
    var dataset = location.hash.substring(location.hash.lastIndexOf("/")+1);

    if (!((battery in suite) && (dataset in suite[battery]))) return;

    var labels = suite[battery][dataset];
    let showcase = document.getElementById("dataset_showcase");
    while (showcase.lastChild) showcase.removeChild(showcase.lastChild);

    let head = document.createElement("h2");
    head.innerHTML = battery + "/" + dataset;
    showcase.appendChild(head);

    for (let l in labels) {
//         let head = document.createElement("h3");
//         head.innerHTML = labels[l];
//         showcase.appendChild(head);

        let figure = document.createElement("figure");
        figure.class = "align-default"

        let img = document.createElement("img");
        img.title = img.alt = labels[l];
        img.src = "../_static/catalogue-v1/" + battery + "/" +
            dataset + "." + labels[l] + ".png";

        figure.appendChild(img);
        showcase.appendChild(figure);
    }

    head = document.createElement("h3");
    head.innerHTML = "Description";
    showcase.appendChild(head);

    let pre = document.createElement("pre");
    pre.id = "dataset_description";
    pre.text = "Description";
    showcase.appendChild(pre);

    let xhr = new XMLHttpRequest();
    xhr.onload = function() {
        document.getElementById("dataset_description").textContent = this.responseText;
    };
    xhr.open("GET", "../_static/catalogue-v1/" + battery + "/" +
            dataset + ".txt");
    xhr.send();
}




window.onhashchange = locationHashChanged;
locationHashChanged();
</script>
::::
