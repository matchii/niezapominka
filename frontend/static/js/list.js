$('document').ready(function() {
    // usuwanie zadania
    $('.delete_button').live('click', function() {
        var id = $(this).parent().attr('task-id')
        $.getJSON('delete_task/', { 'id': id, 'action': 'delete_task' }, function(data) {
            if (data['success']) {
                var obj = $('#task_'+id+'_container').parent()
                obj.fadeOut(300, function() { obj.remove() })
            }
        })
    })
    // skreślanie zadania
    $('.tick_button').live('click', function() {
        var id = $(this).parent().attr('task-id')
        $.getJSON('cross_out_task/', { 'id': id, 'action': 'cross_out_task' }, function(data) {
            if (data['success']) {
                $('#task_'+id).removeClass('tick_button').addClass('revive_button')
                $('#task_'+id).siblings('span.task_name').addClass('cross_gray')
                $('#task_'+id).siblings('div.task_form').hide()
            }
        })
    })
    // odkreślanie (przywracanie) zadania
    $('.revive_button').live('click', function() {
        var id = $(this).parent().attr('task-id')
        $.getJSON('revive_task/', { 'id': id, 'action': 'revive_task' }, function(data) {
            if (data['success']) {
                $('#task_'+id).removeClass('revive_button').addClass('tick_button')
                $('#task_'+id).siblings('span.task_name').removeClass('cross_gray')
                $('#task_'+id).siblings('div.task_form').show().attr('display', 'inline')
            }
        })
    })
    // usuwanie podpunktu
    $('.delete_sub_button').live('click', function() {
        var id = $(this).parent().attr('subtask-id')
        $.getJSON('delete_subtask/', { 'id': id, 'action': 'delete_subtask' }, function(data) {
            if (data['success']) {
                var obj = $('#subtask_'+id+'_container')
                obj.fadeOut(300, function() { obj.remove() })
            }
        })
    })
    // skreślanie podpunktu
    $('.cross_sub_button').live('click', function() {
        var id = $(this).parent().attr('subtask-id')
        $.getJSON('cross_out_subtask/', { 'id': id, 'action': 'cross_out_subtask' }, function(data) {
            if (data['success']) {
                $('#subtask_'+id).removeClass('cross_sub_button').addClass('revive_sub_button')
                $('#subtask_'+id).siblings('span').addClass('cross_gray')
            }
        })
    })
    // odkreślanie (przywracanie) podpunktu
    $('.revive_sub_button').live('click', function() {
        var id = $(this).parent().attr('subtask-id')
        $.getJSON('revive_subtask/', { 'id': id, 'action': 'revive_subtask' }, function(data) {
            if (data['success']) {
                $('#subtask_'+id).removeClass('revive_sub_button').addClass('cross_sub_button')
                $('#subtask_'+id).siblings('span').removeClass('cross_gray')
            }
        })
    })
    // dodawanie podpunktu
    $('.add_button').live('click', function() {
        var id = $(this).parent().parent().attr('task-id')
        var name = $('#subtask_name_'+id).val()
        $.getJSON('add_subtask/', { 'id': id, 'action': 'add_subtask', 'name': name }, function(data) {
            if (data['success']) {
                var new_id = data['id']
                $('#subtask_name_'+id).val('').focus()
                $('#task_'+id+'_container').siblings('div.subtasks_container')
                    .append(
                        $('<div>').addClass('subtask_div').attr('id', 'subtask_'+new_id+'_container')
                            .append($('<button>')
                                .attr({'id': 'del_subtask_'+new_id, 'type': 'button'})
                                .addClass(['delete_sub_button', 'small_button'])
                            ).attr({ 'subtask-id': new_id })
                            .append($('<button>')
                                .attr({'id': 'subtask_'+new_id, 'type': 'button'})
                                .addClass(['cross_sub_button', 'small_button'])
                            ).attr({ 'subtask-id': new_id })
                            .append($('<span>').html(name)
                        )
                    )
            }
        })
    })
    // otwieramy formularzyk wprowadzania nowej wartości priorytetu
    $('.priority').live('click', function() {
        var id = $(this).parent().attr('id')
        var priority = $(this).attr('priority')
        $(this).children('input, button').show().select()
    // filtrujemy wartości z klawiszy
    }).live('keypress', function(event) {
        var charCode = (event.which) ? event.which : event.keyCode;
        // minus jest dozwolony, jeśli jest pierwszym znakiem
        var input = $(this).children('input.priority_input')
        if (charCode == 45 && (input.val().length == 0 || input.val().is(':selected'))) {
            return true
        }
        // Esc chowa formularzyk
        if (charCode == 27) {
            $(this).children('input, button').hide()
            return false
        }
        // Enter wciska przycisk 'zapisz'
        if (charCode == 13) {
            $(this).children('button.set_task_priority_button').click()
            return false;
        }
        // poza tym dopuszczamy tylko cyfry
        if (charCode > 31 && (charCode < 48 || charCode > 57)) {
            return false
        } else {
            return true
        }
    })
    $('.set_task_priority_button').live('click', function() {
        var button = $(this)
        var input = button.siblings('input.priority_input')
        var id = $(this).parent().parent().attr('task-id')
        var priority = input.val()
        $.getJSON(
            'set_task_priority/',
            { 'id': id, 'priority': priority, 'action': 'set_task_priority' },
            function(data) {
                if (data['success']) {
                    location.reload()
                } else {
                    input.hide()
                    button.hide()
                }
            }
        )
    })
});
