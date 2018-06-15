/* ---- FLy our Section For Aria Onepage HTML Template --- */

jQuery(document).ready(function($){
	var $lateral_menu_trigger = $('.nav-trigger'),
		$content_wrapper = $('.main');

	//open-close lateral menu clicking on the menu icon
	$lateral_menu_trigger.on('click', function(event){
		event.preventDefault();

		$lateral_menu_trigger.toggleClass('is-active');
		$content_wrapper.toggleClass('is-active').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function(){
			// firefox transitions break when parent overflow is changed, so we need to wait for the end of the trasition to give the body an overflow hidden
			$('body').toggleClass('overflow-hidden');
		});
		$('#ar-about').toggleClass('is-active');

		//check if transitions are not supported - i.e. in IE9
		if($('html').hasClass('no-csstransitions')) {
			$('body').toggleClass('overflow-hidden');
		}
	});

	//close lateral menu clicking outside the menu itself
	$content_wrapper.on('mouseover', function(event){
		if( !$(event.target).is('.nav-trigger, .nav-trigger span') ) {
			$lateral_menu_trigger.removeClass('is-active');
			$content_wrapper.removeClass('is-active').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function(){
				$('body').removeClass('overflow-hidden');
			});
			$('#ar-about').removeClass('is-active');
			//check if transitions are not supported
			if($('html').hasClass('no-csstransitions')) {
				$('body').removeClass('overflow-hidden');
			}
		}
	});

	
	setInterval( function doIt() {
		var blue = '#2980b9';
	var l = Snap('#logo');
	var p = l.select('path');

	l.append(p);

	p.attr({
		fill: blue,
		stroke: '#0066CC'
	});

		// modify this one line below, and see the result !
		var logoTitle = 'ANONYMIZE CUSTOMER DATA';
		var logoRandom = '';
		var logoTitleContainer = l.text(0, '98%', '');
		var possible = "-+*/|}{[]~\\\":;?/.><=+-_)(*&^%$#@!)}";
		logoTitleContainer.attr({
			fontSize: 250,
			fontFamily: 'Dosis',
			wontWeight: '600',

		});

		function generateRandomTitle(i, logoRandom) {
			setTimeout( function() {
				logoTitleContainer.attr({ text: logoRandom });
			}, i*70 );

		}

		for( var i=0; i < logoTitle.length+1; i++ ) {
			logoRandom = logoTitle.substr(0, i);
			for( var j=i; j < logoTitle.length; j++ ) { 
				logoRandom += possible.charAt(Math.floor(Math.random() * possible.length)); 
			}
			generateRandomTitle(i, logoRandom);
			logoRandom = '';
			// alert("TEXT");
		}
	



	}, 4000 );


	// 	setTimeout(function reset(){
	// 	logoRandom = '';
	// }, 6000);


	// setInterval(reset(), 1000);
    // window.setInterval(reset, 6000);
	// window.setInterval(doIt, 6000);


	

	// setInterval(reset(), 100);

	// setInterval(doIt(), 600);

});
