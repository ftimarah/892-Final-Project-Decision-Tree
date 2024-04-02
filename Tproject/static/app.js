$(document).ready(function () {
  // Function to handle form submission
  $("#transportationForm").submit(function (event) {
    event.preventDefault(); // Prevent default form submission

    // Collect form data
    var formData = {
      startLocation: $("#startLocation").val(),
      endLocation: $("#endLocation").val(),
      distance: $("#distance").val(),
      urgency: $("#urgency").val(),
    };

    // Send POST request to Flask server
    $.ajax({
      type: "POST",
      url: "/predict",
      contentType: "application/json",
      data: JSON.stringify(formData),
      error: function (error) {
        console.error("Error:", error);
      },
    }).done(function() {
      window.location.href = "/result";
      console.log('sent');
    })
  });
});
