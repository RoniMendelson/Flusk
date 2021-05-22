
function CreateUsersList(users){
    console.log(users);
    const user=users[0];
    console.log(user);
    const curr_main=document.querySelector("main");
    for (let user of users){
        const section=document.createElement('section');
        section.innerHTML=`
            <img src="${user.avatar}" alt="profile picture"/>
        <div>
        <span>${user.first_name} ${user.last_name}</span>
            <br>
                <a href="mailto:${user.email}">Email</a>
        </div>`
        curr_main.appendChild(section);
    }

}
fetch('https://reqres.in/api/users?page=2').then(
    response=>response.json()
).then(
    responseOBJECT=>CreateUsersList(responseOBJECT.data)
)
    .catch(err => console.log(err));