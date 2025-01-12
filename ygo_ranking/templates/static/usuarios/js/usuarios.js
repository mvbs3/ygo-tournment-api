function copyToClipboard(event, text) {
    event.preventDefault();
    
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
  }

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