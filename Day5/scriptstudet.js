function onFormSubmit() {
  const name = document.getElementById("NAME").value.trim();
  const age = document.getElementById("AGE").value.trim();
  const mobile = document.getElementById("MOBILE").value.trim();
  const email = document.getElementById("MailID").value.trim();
  const course = document.getElementById("COURSE").value.trim();

  if (isValid(name, age, mobile, email, course)) {
    alert("Your details are saved successfully!");
    clearForm();
  }
}

function isValid(name, age, mobile, email, course) {
  // Name
  const namePattern = /^[a-zA-Z\s]+$/;
  if (!namePattern.test(name)) {
    alert("Please enter a valid Name (letters and spaces only).");
    return false;
  }

  // Age
  const ageValue = parseInt(age);
  if (isNaN(ageValue) || ageValue < 1 || ageValue > 120) {
    alert("Please enter a valid Age between 1 and 120.");
    return false;
  }

  // Mobile
  const mobilePattern = /^[6-9]\d{9}$/;
  if (!mobilePattern.test(mobile)) {
    alert("Please enter a valid 10-digit Mobile number ");
    return false;
  }

  // Email
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailPattern.test(email)) {
    alert("Please enter a valid Email ID.");
    return false;
  }

  // Course
  const coursePattern = /^[a-zA-Z0-9\s]+$/;
  if (!coursePattern.test(course)) {
    alert("Please enter a valid Course name (letters and spaces only).");
    return false;
  }
  return true;
}

function clearForm() {
  document.getElementById("NAME").value = "";
  document.getElementById("AGE").value = "";
  document.getElementById("MOBILE").value = "";
  document.getElementById("MailID").value = "";
  document.getElementById("COURSE").value = "";
}

function exitForm() {
  if (confirm("Are you sure you want to exit?")) {
    alert("Exiting the form");
  }
}
