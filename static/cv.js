    function onHover()
    {
        $("#news").attr('src', 'Me.JPG');
    }

    function offHover()
    {
        $("#news").attr('src', 'Me1.JPG');
    }

function showText(Item2Det)
    {
        document.getElementById(Item2Det).style.display = "block";
    }
    function showText(Item3Res)
    {
        document.getElementById(Item3Res).style.display = "block";
    }
fetch('https://reqres.in/api/users?page=2').then(
    response=>response.json()
).then(
    responseOBJECT=>CreateUsersList(responseOBJECT.data)
)
    .catch(err => console.log(err));

