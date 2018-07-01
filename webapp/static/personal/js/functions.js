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

  $('#collapsible-panels a').click(function(e) {
    var clicked = $(this).attr('id');
    if (clicked == "graph2017")
      convertChartLine17();
    if (clicked == "line")
      convertChartLine();
    else
      convertChartBar();


    //slide down the corresponding div if hidden, or slide up if shown
    $(this).parent().next('#collapsible-panels div').slideToggle('slow');
    //set the current item as active
    //$(this).parent().toggleClass('active')
    e.preventDefault()
  })

  // append click event to the a element

})
