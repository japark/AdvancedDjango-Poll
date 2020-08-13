document.addEventListener('DOMContentLoaded', function () { 

	function newGenerateForm (totalForms, formset, formSel) {
		const cnt = totalForms.value;
		let cloned = formset.querySelector(formSel).cloneNode(true);
		let labels = cloned.querySelectorAll('label');
		let inputs = cloned.querySelectorAll('input');
		
		if (labels.length != 0) {
			labels.forEach((label) => {
				let labelSplit = label.getAttribute('for').split('-');
				labelSplit[1] = cnt;
				label.setAttribute('for', labelSplit.join('-'));
			});
		}
		
		if (inputs.length != 0) {
			inputs.forEach((input) => {
				input.value = "";
				let inputSplit = input.name.split('-');
				inputSplit[1] = cnt;
				input.name = inputSplit.join('-');
				inputSplit = input.id.split('-');
				inputSplit[1] = cnt;
				input.id = inputSplit.join('-');
			});
		}

		// Create "Delete" Button.
		let spanTag = document.createElement('span');
		spanTag.innerText = ' ';
		cloned.appendChild(spanTag);
		let deleteBtn = document.createElement('a');
		deleteBtn.className = 'delete-choice';
		deleteBtn.innerText = '삭제';
		cloned.appendChild(deleteBtn);

		// Append new form at the end of existing forms
		// and increase the total number of forms.
		totalForms.value = String(Number(cnt) + 1);
		formset.appendChild(cloned);

		deleteBtnReset(totalForms, formSel);
		return cloned;
	}


	function deleteBtnReset (totalForms, formSel) {
		let form;
		let deleteBtns = document.querySelectorAll('.delete-choice');
		deleteBtns.forEach((deleteBtn) => {
			deleteBtn.onclick = function (e) {
				do {
					form = e.srcElement.parentElement;
				} while (!form.classList.contains(formSel.split('.')[1]));
				const cnt = totalForms.value;
				totalForms.value = String(Number(cnt) - 1);
				form.remove();
				arrangeOrder(formSel);
			};
		});
	}


	function arrangeOrder (formSel) {
		let forms = document.querySelectorAll(formSel);
		forms.forEach((form, idx) => {
			let labels = form.querySelectorAll('label');
			let inputs = form.querySelectorAll('input');
			if (labels.length != 0) {
				labels.forEach((label) => {
					let labelSplit = label.getAttribute('for').split('-');
					labelSplit[1] = idx;
					label.setAttribute('for', labelSplit.join('-'));
				});
			}
			if (inputs.length != 0) {
				inputs.forEach((input) => {
					let inputSplit = input.name.split('-');
					inputSplit[1] = idx;
					input.name = inputSplit.join('-');
					inputSplit = input.id.split('-');
					inputSplit[1] = idx;
					input.id = inputSplit.join('-');
				});
			}
		});
	}


	const modelname = 'Choice';
	const formsetSel = '.choice-formset';
	const formSel = '.choice-form';
	const name = modelname.toLowerCase();
	let formset = document.querySelector(formsetSel);
	let totalForms = formset.querySelector('input[name=' + name + '_set-TOTAL_FORMS]');
	let initialForms = formset.querySelector('input[name=' + name + '_set-INITIAL_FORMS]');
	initialForms.value = '0';

	let addBtn = document.querySelector('.add-choice');
	addBtn.onclick = function () {
		newGenerateForm(
			totalForms,
			formset,
			formSel
		)
	};
	deleteBtnReset(totalForms, formSel);

}, false);
