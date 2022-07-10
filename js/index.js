function takeTest() {
    document.querySelector('#takeTest').style.display = 'block';

    document.querySelector('takeTestForm').addEventListener('submit', (event) => {
        event.preventDefault();

        //get test value
        let testLink = document.querySelector('#test_link').value;
        document.querySelector('#test_link').value = '';

        //route to new page
        //TODO
        window.location.replace(`/${testLink}/`);
        //window.location = `/${testLink}/`;
    });
}

