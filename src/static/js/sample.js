window.addEventListener('load',
    function (event) {
        document.getElementById('click').addEventListener('click',
            function() {
                alert('Hello');
            }
        , false);
    }
, false);
