// charts.js

// Financial Overview Chart
var financialOverviewData = {
    labels: ['Debt', 'Income', 'Investment', 'Bank Balance'],
    datasets: [{
        data: [{{ user_profile.credit_card_debt|add:user_profile.mortgage_value|add:user_profile.car_loan|add:user_profile.student_loan }},
               {{ user_profile.salary }},
               {{ user_profile.stocks_value|add:user_profile.bonds_value|add:user_profile.cryptocurrency_balance }},
               41881.82],
        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0']
    }]
};

var financialOverviewChartCanvas = document.getElementById('financial-overview-chart').getContext('2d');
var financialOverviewChart = new Chart(financialOverviewChartCanvas, {
    type: 'bar',
    data: financialOverviewData,
});

// Expenses Chart
var expensesData = {
    labels: [{% for expense in expenses %}'{{ expense.description }}',{% endfor %}],
    datasets: [{
        data: [{% for expense in expenses %}{{ expense.amount }},{% endfor %}],
        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9900']
    }]
};

var expensesChartCanvas = document.getElementById('expenses-chart').getContext('2d');
var expensesChart = new Chart(expensesChartCanvas, {
    type: 'doughnut',
    data: expensesData,
});
