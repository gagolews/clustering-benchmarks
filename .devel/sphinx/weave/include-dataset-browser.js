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
        img.style = 'width: inherit';
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
