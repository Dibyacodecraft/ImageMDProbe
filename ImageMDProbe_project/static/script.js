document.getElementById('imageInput').addEventListener('change', function() {
  const file = this.files[0];
  const imageElement = document.getElementById('uploadedImage');

  if (file) {
    imageElement.src = URL.createObjectURL(file);
  } else {
    imageElement.src = '#';
    alert('Please select an image file.');
  }
});

document.getElementById('uploadBtn').addEventListener('click', function() {
  const fileInput = document.getElementById('imageInput');
  const file = fileInput.files[0];

  if (file) {
    const formData = new FormData();
    formData.append('image', file);

    fetch('/diagnose', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      const resultArea = document.getElementById('diagnosisResult');
      if (data.diagnosis) {
        resultArea.textContent = `The diagnosis result is: ${data.diagnosis}`;
      } else {
        resultArea.textContent = 'Error: Unable to diagnose.';
      }
    })
    .catch(error => console.error('Error:', error));
  } else {
    alert('Please select an image file.');
  }
});
