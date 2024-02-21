function makePrediction() {
    const satisfaction_level = parseFloat(document.getElementById('satisfaction_level').value);
    const last_evaluation = parseFloat(document.getElementById('last_evaluation').value);
    const number_project = parseInt(document.getElementById('number_project').value);
    const average_monthly_hours = parseInt(document.getElementById('average_monthly_hours').value);
    const time_spend_company = parseInt(document.getElementById('time_spend_company').value);
    const work_accident = parseInt(document.getElementById('work_accident').value);
    const promotion_last_5years = parseInt(document.getElementById('promotion_last_5years').value);
    const departments = document.getElementById('departments').value; // No need to convert
    const salary = document.getElementById('salary').value; // No need to convert

    const data = {
        satisfaction_level: satisfaction_level,
        last_evaluation: last_evaluation,
        number_project: number_project,
        average_monthly_hours: average_monthly_hours,
        time_spend_company: time_spend_company,
        work_accident: work_accident,
        promotion_last_5years: promotion_last_5years,
        departments: departments,
        salary: salary
    };
    console.log(data);

    fetch('http://127.0.0.1:12345/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        mode: 'cors',
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        const prediction = parseInt(data.prediction);
        console.log(prediction);
        document.getElementById('prediction-text').textContent = prediction;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}