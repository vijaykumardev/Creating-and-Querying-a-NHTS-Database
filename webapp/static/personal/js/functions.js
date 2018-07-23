function downloadCSV(csv, filename) {
  var csvFile;
  var downloadLink;

  // CSV file
  csvFile = new Blob([csv], {
    type: "text/csv"
  });

  // Download link
  downloadLink = document.createElement("a");

  // File name
  downloadLink.download = filename;

  // Create a link to the file
  downloadLink.href = window.URL.createObjectURL(csvFile);

  // Hide download link
  downloadLink.style.display = "none";

  // Add the link to DOM
  document.body.appendChild(downloadLink);

  // Click download link
  downloadLink.click();
}

function exportTableToCSV(filename, idSelector) {
  var csv = [];
  console.log(idSelector + " tr");
  var rows = document.querySelectorAll(idSelector + " tr");
  console.log(rows);
  for (var i = 0; i < rows.length; i++) {
    var row = [],
      cols = rows[i].querySelectorAll("td, th");

    for (var j = 0; j < cols.length; j++)
      row.push('"' + cols[j].innerText + '"');

    csv.push(row.join(","));
  }

  // Download CSV file
  downloadCSV(csv.join("\n"), filename);
}

function convertChartLine(renderAt,idName,type,chartID) {
  var getTabularData = function() {
    var table = document.getElementById(idName),
      rows = table.children[0].children,
      row,
      i,
      length,
      data = [];
    // get the table element and iterate over its children and extract the data
    for (i = 1, length = rows.length; i < length; i++) {

      row = rows[i];
      data.push({
        label: row.children[0].innerHTML,
        value: row.children[1].innerHTML
      });
    }

    return data;
  };
  var revenueChart = new FusionCharts({
    type: type,
    renderAt: renderAt+"-render",
    width: '1000',
    height: '450',
    dataFormat: 'json',
    id: 'line-chart',
    dataSource: {
      "chart": {
        "caption": $("#"+renderAt).attr("title"),
        "subCaption": "",
        "xAxisName":$("#"+renderAt).attr("x-axis"),
        "yAxisName": $("#"+renderAt).attr("y-axis"),
        "numberPrefix": "",
        "theme": "fint",
        "rotateValues": "1",
        "exportEnabled": "1"
      },
      "data": getTabularData()
    }
  });
  revenueChart.render();
}
function convertChartBar(renderAt,idName) {
    var getTabularData = function() {
    var table = document.getElementById(idName),
      rows = table.children[0].children,
      row,
      i,
      length,
      data = [];
    // get the table element and iterate over its children and extract the data
    for (i = 1, length = rows.length; i < length; i++) {

      row = rows[i];
      data.push({
        label: row.children[0].innerHTML,
        value: row.children[1].innerHTML
      });
    }

    return data;
  };
  var revenueChart2D = new FusionCharts({
    type: 'column2D',
    renderAt: renderAt,
    width: '1000',
    height: '450',
    dataFormat: 'json',
    id: 'bar-chart',
    dataSource: {
      "chart": {
        "caption": caption,
        "subCaption": "",
        "xAxisName": 'state',
        "yAxisName": yAxisName,
        "numberPrefix": "",
        "theme": "fint",
        "rotateValues": "1",
        "exportEnabled": "1"
      },
      "data": getTabularData()
    }
  });
  revenueChart2D.render();
}


/**
 * submit the form of a page when option is selected
 * * @param  {string}  formName     name of the form where the option is selected
 */
function changeTextBox(formName) {
  var x = document.getElementsByName(formName);
  x[0].submit();
}

$(document).ready(function() {
  //hide all divecontainers
  $('#collapsible-panels div').hide()

  //convertChartBar();
  $('#collapsible-panels a').click(function(e) {
    var clicked = $(this).attr('id');
    var chartType = $("#"+clicked).attr("type");
    if (clicked == "line-2017"  || clicked == "bar-2017"){
      convertChartLine(clicked,"dataTable17",chartType,"chart-line");
    }
    else if (clicked == "line-2009" || clicked == "bar-2009"){
      convertChartLine(clicked,"dataTable",chartType,"chart-line");
    }

    //slide down the corresponding div if hidden, or slide up if shown
    $(this).parent().next('#collapsible-panels div').slideToggle('slow');
    //set the current item as active
    //$(this).parent().toggleClass('active')
    e.preventDefault()
  })

  // append click event to the a element

})
