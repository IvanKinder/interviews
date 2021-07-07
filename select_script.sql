select department from employees
where `position` = 'Software Developer'
group by department
having count(`position`) < 5;
