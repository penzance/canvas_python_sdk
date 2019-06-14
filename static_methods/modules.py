from canvas_sdk import client, utils

def create_module(request_ctx, course_id, module_name, module_unlock_at=None, module_position=None, module_require_sequential_progress=None, module_prerequisite_module_ids=None, module_publish_final_grade=None, **request_kwargs):
    """
    Create and return a new module

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param module_name: (required) The name of the module
        :type module_name: string
        :param module_unlock_at: (optional) The date the module will unlock
        :type module_unlock_at: datetime or None
        :param module_position: (optional) The position of this module in the course (1-based)
        :type module_position: integer or None
        :param module_require_sequential_progress: (optional) Whether module items must be unlocked in order
        :type module_require_sequential_progress: boolean or None
        :param module_prerequisite_module_ids: (optional) IDs of Modules that must be completed before this one is unlocked. Prerequisite modules must precede this module (i.e. have a lower position value), otherwise they will be ignored
        :type module_prerequisite_module_ids: string or None
        :param module_publish_final_grade: (optional) Whether to publish the student's final grade for the course upon completion of this module.
        :type module_publish_final_grade: boolean or None
        :return: Create a module
        :rtype: requests.Response (with Module data)

    """

    path = '/v1/courses/{course_id}/modules'
    payload = {
        'module[name]' : module_name,
        'module[unlock_at]' : module_unlock_at,
        'module[position]' : module_position,
        'module[require_sequential_progress]' : module_require_sequential_progress,
        'module[prerequisite_module_ids]' : module_prerequisite_module_ids,
        'module[publish_final_grade]' : module_publish_final_grade,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_module(request_ctx, course_id, id, module_name=None, module_unlock_at=None, module_position=None, module_require_sequential_progress=None, module_prerequisite_module_ids=None, module_publish_final_grade=None, module_published=None, **request_kwargs):
    """
    Update and return an existing module

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param module_name: (optional) The name of the module
        :type module_name: string or None
        :param module_unlock_at: (optional) The date the module will unlock
        :type module_unlock_at: datetime or None
        :param module_position: (optional) The position of the module in the course (1-based)
        :type module_position: integer or None
        :param module_require_sequential_progress: (optional) Whether module items must be unlocked in order
        :type module_require_sequential_progress: boolean or None
        :param module_prerequisite_module_ids: (optional) IDs of Modules that must be completed before this one is unlocked Prerequisite modules must precede this module (i.e. have a lower position value), otherwise they will be ignored
        :type module_prerequisite_module_ids: string or None
        :param module_publish_final_grade: (optional) Whether to publish the student's final grade for the course upon completion of this module.
        :type module_publish_final_grade: boolean or None
        :param module_published: (optional) Whether the module is published and visible to students
        :type module_published: boolean or None
        :return: Update a module
        :rtype: requests.Response (with Module data)

    """

    path = '/v1/courses/{course_id}/modules/{id}'
    payload = {
        'module[name]' : module_name,
        'module[unlock_at]' : module_unlock_at,
        'module[position]' : module_position,
        'module[require_sequential_progress]' : module_require_sequential_progress,
        'module[prerequisite_module_ids]' : module_prerequisite_module_ids,
        'module[publish_final_grade]' : module_publish_final_grade,
        'module[published]' : module_published,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response
