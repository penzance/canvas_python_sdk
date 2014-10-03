"""
if you ran the generate_sdk_methods.py script you will need to
replace the coresponding methods in courses.py with these. You need
to also check to see if there were any other changes, it may not be a simple
cut and paste.
"""

def copy_course_content(request_ctx, course_id, source_course, var_except, only, **request_kwargs):
    """
    DEPRECATED: Please use the `ContentMigrationsController#create <https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_migrations_controller.rb>`_
    
    Copies content from one course into another. The default is to copy all course
    content. You can control specific types to copy by using either the 'except' option
    or the 'only' option.
    
    The response is the same as the course copy status endpoint

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param source_course: (required) ID or SIS-ID of the course to copy the content from
        :type source_course: string
        :param except: (required) A list of the course content types to exclude, all areas not listed will be copied.
        :type except: string
        :param only: (required) A list of the course content types to copy, all areas not listed will not be copied.
        :type only: string
        :return: Copy course content
        :rtype: requests.Response (with void data)

    """

    except_types = ('course_settings', 'assignments', 'external_tools', 'files', 'topics', 'calendar_events', 'quizzes', 'wiki_pages', 'modules', 'outcomes')
    only_types = ('course_settings', 'assignments', 'external_tools', 'files', 'topics', 'calendar_events', 'quizzes', 'wiki_pages', 'modules', 'outcomes')
    utils.validate_attr_is_acceptable(var_except, except_types)
    utils.validate_attr_is_acceptable(only, only_types)
    path = '/v1/courses/{course_id}/course_copy'
    payload = {
        'source_course' : source_course,
        'except' : var_except,
        'only' : only,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response
