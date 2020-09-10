/**
 * Get data from expertise.json, perform some processing.
 */

/*
Global Variables
 */
var data_location = 'expertise.json';
var json_data;

/*
Get Data from json
*/
function getData () {


    json_data = (function () {
        json_data = null;
        $.ajax({
            'async': false,
            'global': false,
            'url': data_location,
            'dataType': "json",
            'success': function (data) {
                json_data = data;
            }
        });
        console.log(json_data.law)
        return json_data;
    })();
}

function processData () {

    document.getElementById('last_updated').innerHTML = json_data.last_update;

    // document.getElementById('data').innerHTML = json_data.law;
    //
    if(json_data.law){
        var len = json_data.law.length;
        var txt = "";
        if(len > 0){
            for(var i=0;i<len;i++){
                txt += "<tr><td>"+json_data.law[i].name +"</td><td>"+json_data.law[i].expertise+"</td></tr>";
            }
            if(txt != ""){
                $("#table").append(txt).removeClass("hidden");
            }
        }
    }
}

getData();
processData();
