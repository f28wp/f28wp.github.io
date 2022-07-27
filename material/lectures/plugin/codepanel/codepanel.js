

let style = document.createElement('style');
document.head.appendChild( style );
style.textContent = `
.slider {
    position: absolute;
    overflow: hidden;
    z-index:  10000;

    visibility: hidden;
}

/* --------------------------- */

.slider.bottom {
    top: 100%;
    left: 0px;
    transition: top 1s;
    height: 100%;
    width:  100%;
    background: blue;
    color: cyan;
}

.slider.bottom.in {
    top: 0%;
}
/* ------------------------------ */

@media print {
   .noprint{
	   visibility: hidden !important;
       display:none;
   }
}


`;

/*
// src="https://jsitor.com/"

// https://esnextb.in/

// src="https://cssdeck.com/"

// src="https://liveweave.com/"

*/
function setupcodepanel( sid, surl )
{
	if ( sid  == undefined ) sid = 0;
	if ( surl == undefined ) surl = 'https://liveweave.com/';
	
	let div = document.createElement('div');
	document.body.appendChild( div );
	div.id        = 'sliderpanel' + sid;
	div.className = 'noprint bottom slider';
	div.innerHTML = `<iframe height="100%" style="width: 100%;" 
					  scrolling="yes" title="F28WP" 
					  class="noprint"
					  src="${surl}"
					  frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
		 </iframe> 
		 `;
}


function togglecodepanel( sid )
{
   if ( sid == undefined ) sid = 0;
   console.log( 'togglecodepanel sid:', sid );
   
   // toggle 'all' sliderpanels to off 
   
   let els = document.getElementsByClassName( 'slider' );
   for (let i=0; i<els.length; i++)
   {
	 els[i].style['visibility'] = 'visible';
	   
	 if ( els[i].id == 'sliderpanel' + sid ) continue;
	 
     if ( els[i].classList.contains( 'in' ) )
     {
        els[i].classList.remove('in');
     }

   }// end for i
   

   let el = document.getElementById( 'sliderpanel' + sid );
   if ( el.classList.contains( 'in' ) )
   {
	   el.classList.remove('in');
   }
   else 
   {
	   el.classList.add('in');
   }   
}
//console.log('toggle panel ready ...');


//function togglecodepanel( sid )
//{
//	slider("sliderpanel");
//}



/*	
Reveal.addEventListener( 'slidechanged', function( event ) {

	tts.Read();
}
);
	
	
Reveal.addEventListener( 'fragmentshown', function( event ) {
// This reads the text content of fragments as they are shown.
// event.fragment = the fragment element
	if (tts.readFrags && tts.On){
		let txt = event.fragment.textContent;
		tts.ReadText(txt);
	}
	} );
	
	
Reveal.configure({
  keyboard: {
    81: function() {tts.Synth.cancel()}, // press q to cancel speaking and clear speech queue.
	84: function() {tts.ToggleSpeech()}  // press t to toggle speech on/off
					 
  }
});
*/