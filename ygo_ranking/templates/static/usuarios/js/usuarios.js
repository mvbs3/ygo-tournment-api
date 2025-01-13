function copyToClipboard(event, text) {
    event.preventDefault();
    
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
  }

var csrf_token = document.cookie.match(/csrftoken=([^;]*)/)[1];

form_to_show = {"criar_duelista": 1, "atualizar_duelista": 2}
function show_form(form_show){
    show_duelist = document.getElementById("show-duelist")
    show_deck = document.getElementById("show-deck")
    att_duelist = document.getElementById("att_duelist")
    console.log(form_show)
    if (form_show == "1"){
        att_duelist.style.display = "none"
        show_duelist.style.display = "block"
        show_deck.style.display = "block"
        
    }else if (form_show == "2"){
        show_duelist.style.display = "none"
        show_deck.style.display = "none"
        
        att_duelist.style.display = "block"
        console.log(att_duelist)
        
        
    }
    

}

function atualizar_meu_duelist(id){
    console.log("eu estou entrando na function")
    nome = document.getElementById("nome").value
    nickname = document.getElementById("nickname").value
    email = document.getElementById("email").value
    cossyId = document.getElementById("cossyId").value
    contact_number = document.getElementById("contact_number").value
   fetch('/duelists/atualizar_duelist/' + id,{
       method:"POST",
       headers: {
           'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            "name": nome,
            "nickname": nickname,
            "email": email,
            "cossyId": cossyId,
            "contact_number": contact_number
        })
   }).then(function(result){
       return result.json()
   }).then(function(data){
        if(data['status'] == "200"){
            nome = data['name'] 
            nickname = data['nickname']
            email = data['email']
            cossyId = data['cossyId']
            contact_number = data['contact_number']
            alert("Duelista atualizado com sucesso")
            window.location.href = '/usuarios/meu_perfil/';

        }
       console.log(data)
   })
}

    