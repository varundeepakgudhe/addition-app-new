document.getElementById('addition-form').addEventListener('submit', async (event) => {
    event.preventDefault();
  
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
  
    const response = await fetch('https://addition-app-a8d5117c8a8e.herokuapp.com/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ num1, num2 }),
      });
    // const response = await fetch('http://127.0.0.1:5000/add', {
    //   method: 'POST',
    //   headers: {
    //       'Content-Type': 'application/json',
    //   },
    //   body: JSON.stringify({ num1, num2 }),
    //   }); 
  
    const result = await response.json();
    if (response.ok) {
      document.getElementById('result').textContent = `Result: ${result.result}`;
    } else {
      document.getElementById('result').textContent = `Error: ${result.error}`;
    }
  });
  