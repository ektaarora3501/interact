

var skills = ["Build" ,"Design" ,"Code" , "Develope", "Think","Study","Strike","Create","Dare"];
	var just = setInterval(change, 500,skills);
	var i =0;
	
	function change(skills) {
		  var t = skills[i]
		  console.log(i);
		  document.getElementById("demo").innerHTML = "<span class='one'>" + t+"</span>";
		  i=i +1;
		  console.log("i="+i)
        
		  if(i== skills.length){
		  	i = 0;
		  }
		}

