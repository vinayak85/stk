// Copyright (c) 2018, vin and contributors
// For license information, please see license.txt

frappe.ui.form.on('test2', {
	refresh: function(frm) {

	},
	process_1:function (frm) {
		frappe.call({
			method:'stkapp.stkapp.doctype.test2.test2.auth',
			args:{
				
			},
			callback:function (r) {
				
			}
		});
	}
});
