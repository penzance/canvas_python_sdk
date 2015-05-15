
"""
The methods in this file have been altered outside the scope of the generate script either
because the Canvas documentation is not up to date or for some other reason.

Copy methods in this file to overwrite the same methods in the courses.py module in the methods folder.
"""

def create_new_course(request_ctx, account_id, course_name=None, course_course_code=None, course_start_at=None, course_end_at=None, course_license=None, course_is_public=None, course_is_public_to_auth_users=None, course_public_syllabus=None, course_public_description=None, course_allow_student_wiki_edits=None, course_allow_wiki_comments=None, course_allow_student_forum_attachments=None, course_open_enrollment=None, course_self_enrollment=None, course_restrict_enrollments_to_course_dates=None, course_term_id=None, course_sis_course_id=None, course_integration_id=None, course_hide_final_grades=None, course_apply_assignment_group_weights=None, offer=None, enroll_me=None, course_syllabus_body=None, **request_kwargs):
    """
    Create a new course

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) The unique ID of the account to create to course under.
        :type account_id: integer
        :param course_name: (optional) The name of the course. If omitted, the course will be named "Unnamed Course."
        :type course_name: string or None
        :param course_course_code: (optional) The course code for the course.
        :type course_course_code: string or None
        :param course_start_at: (optional) Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z
        :type course_start_at: datetime or None
        :param course_end_at: (optional) Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z
        :type course_end_at: datetime or None
        :param course_license: (optional) The name of the licensing. Should be one of the following abbreviations (a descriptive name is included in parenthesis for reference): - 'private' (Private Copyrighted) - 'cc_by_nc_nd' (CC Attribution Non-Commercial No Derivatives) - 'cc_by_nc_sa' (CC Attribution Non-Commercial Share Alike) - 'cc_by_nc' (CC Attribution Non-Commercial) - 'cc_by_nd' (CC Attribution No Derivatives) - 'cc_by_sa' (CC Attribution Share Alike) - 'cc_by' (CC Attribution) - 'public_domain' (Public Domain).
        :type course_license: string or None
        :param course_is_public: (optional) Set to true if course if public.
        :type course_is_public: boolean or None
        :param course_is_public_to_auth_users: (optional) Set to true if course if public to autorized users.
        :type course_is_public_to_auth_users: boolean or None
        :param course_public_syllabus: (optional) Set to true to make the course syllabus public.
        :type course_public_syllabus: boolean or None
        :param course_public_description: (optional) A publicly visible description of the course.
        :type course_public_description: string or None
        :param course_allow_student_wiki_edits: (optional) If true, students will be able to modify the course wiki.
        :type course_allow_student_wiki_edits: boolean or None
        :param course_allow_wiki_comments: (optional) If true, course members will be able to comment on wiki pages.
        :type course_allow_wiki_comments: boolean or None
        :param course_allow_student_forum_attachments: (optional) If true, students can attach files to forum posts.
        :type course_allow_student_forum_attachments: boolean or None
        :param course_open_enrollment: (optional) Set to true if the course is open enrollment.
        :type course_open_enrollment: boolean or None
        :param course_self_enrollment: (optional) Set to true if the course is self enrollment.
        :type course_self_enrollment: boolean or None
        :param course_restrict_enrollments_to_course_dates: (optional) Set to true to restrict user enrollments to the start and end dates of the course.
        :type course_restrict_enrollments_to_course_dates: boolean or None
        :param course_term_id: (optional) The unique ID of the term to create to course in.
        :type course_term_id: integer or None
        :param course_sis_course_id: (optional) The unique SIS identifier.
        :type course_sis_course_id: string or None
        :param course_integration_id: (optional) The unique Integration identifier.
        :type course_integration_id: string or None
        :param course_hide_final_grades: (optional) If this option is set to true, the totals in student grades summary will be hidden.
        :type course_hide_final_grades: boolean or None
        :param course_apply_assignment_group_weights: (optional) Set to true to weight final grade based on assignment groups percentages.
        :type course_apply_assignment_group_weights: boolean or None
        :param offer: (optional) If this option is set to true, the course will be available to students immediately.
        :type offer: boolean or None
        :param enroll_me: (optional) Set to true to enroll the current user as the teacher.
        :type enroll_me: boolean or None
        :param course_syllabus_body: (optional) The syllabus body for the course
        :type course_syllabus_body: string or None
        :return: Create a new course
        :rtype: requests.Response (with Course data)

    """

    path = '/v1/accounts/{account_id}/courses'
    payload = {
        'course[name]' : course_name,
        'course[course_code]' : course_course_code,
        'course[start_at]' : course_start_at,
        'course[end_at]' : course_end_at,
        'course[license]' : course_license,
        'course[is_public]' : course_is_public,
        'course[is_public_to_auth_users]' : course_is_public_to_auth_users,
        'course[public_syllabus]' : course_public_syllabus,
        'course[public_description]' : course_public_description,
        'course[allow_student_wiki_edits]' : course_allow_student_wiki_edits,
        'course[allow_wiki_comments]' : course_allow_wiki_comments,
        'course[allow_student_forum_attachments]' : course_allow_student_forum_attachments,
        'course[open_enrollment]' : course_open_enrollment,
        'course[self_enrollment]' : course_self_enrollment,
        'course[restrict_enrollments_to_course_dates]' : course_restrict_enrollments_to_course_dates,
        'course[term_id]' : course_term_id,
        'course[sis_course_id]' : course_sis_course_id,
        'course[integration_id]' : course_integration_id,
        'course[hide_final_grades]' : course_hide_final_grades,
        'course[apply_assignment_group_weights]' : course_apply_assignment_group_weights,
        'offer' : offer,
        'enroll_me' : enroll_me,
        'course[syllabus_body]' : course_syllabus_body,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response

def update_course(request_ctx, id, course_account_id=None, course_name=None, course_course_code=None, course_start_at=None, course_end_at=None, course_license=None, course_is_public=None, course_is_public_to_auth_users=None, course_public_syllabus=None, course_public_description=None, course_allow_student_wiki_edits=None, course_allow_wiki_comments=None, course_allow_student_forum_attachments=None, course_open_enrollment=None, course_self_enrollment=None, course_restrict_enrollments_to_course_dates=None, course_term_id=None, course_sis_course_id=None, course_integration_id=None, course_hide_final_grades=None, course_apply_assignment_group_weights=None, offer=None, course_syllabus_body=None, course_grading_standard_id=None, course_course_format=None, **request_kwargs):

    """
    Update an existing course.

    For possible arguments, see the Courses#create documentation (note: the enroll_me param is not allowed in the update action).

    Additional arguments available for Courses#update
        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param account_id: (optional) The unique ID of the account to move course into. If ommitted, do not change the course's account.
        :type account_id: integer
        :param course_name: (optional) The name of the course. If omitted, the course will be named "Unnamed Course."
        :type course_name: string or None
        :param course_course_code: (optional) The course code for the course.
        :type course_course_code: string or None
        :param course_start_at: (optional) Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z
        :type course_start_at: datetime or None
        :param course_end_at: (optional) Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z
        :type course_end_at: datetime or None
        :param course_license: (optional) The name of the licensing. Should be one of the following abbreviations (a descriptive name is included in parenthesis for reference): - 'private' (Private Copyrighted) - 'cc_by_nc_nd' (CC Attribution Non-Commercial No Derivatives) - 'cc_by_nc_sa' (CC Attribution Non-Commercial Share Alike) - 'cc_by_nc' (CC Attribution Non-Commercial) - 'cc_by_nd' (CC Attribution No Derivatives) - 'cc_by_sa' (CC Attribution Share Alike) - 'cc_by' (CC Attribution) - 'public_domain' (Public Domain).
        :type course_license: string or None
        :param course_is_public: (optional) Set to true if course if public.
        :type course_is_public: boolean or None
        :param course_public_syllabus: (optional) Set to true to make the course syllabus public.
        :type course_public_syllabus: boolean or None
        :param course_public_description: (optional) A publicly visible description of the course.
        :type course_public_description: string or None
        :param course_allow_student_wiki_edits: (optional) If true, students will be able to modify the course wiki.
        :type course_allow_student_wiki_edits: boolean or None
        :param course_allow_wiki_comments: (optional) If true, course members will be able to comment on wiki pages.
        :type course_allow_wiki_comments: boolean or None
        :param course_allow_student_forum_attachments: (optional) If true, students can attach files to forum posts.
        :type course_allow_student_forum_attachments: boolean or None
        :param course_open_enrollment: (optional) Set to true if the course is open enrollment.
        :type course_open_enrollment: boolean or None
        :param course_self_enrollment: (optional) Set to true if the course is self enrollment.
        :type course_self_enrollment: boolean or None
        :param course_restrict_enrollments_to_course_dates: (optional) Set to true to restrict user enrollments to the start and end dates of the course.
        :type course_restrict_enrollments_to_course_dates: boolean or None
        :param course_term_id: (optional) The unique ID of the term to create to course in.
        :type course_term_id: integer or None
        :param course_sis_course_id: (optional) The unique SIS identifier.
        :type course_sis_course_id: string or None
        :param course_integration_id: (optional) The unique Integration identifier.
        :type course_integration_id: string or None
        :param course_hide_final_grades: (optional) If this option is set to true, the totals in student grades summary will be hidden.
        :type course_hide_final_grades: boolean or None
        :param course_apply_assignment_group_weights: (optional) Set to true to weight final grade based on assignment groups percentages.
        :type course_apply_assignment_group_weights: boolean or None
        :param offer: (optional) If this option is set to true, the course will be available to students immediately.
        :type offer: boolean or None
        :param enroll_me: (optional) Set to true to enroll the current user as the teacher.
        :type enroll_me: boolean or None
        :param course_syllabus_body: (optional) The syllabus body for the course
        :type course_syllabus_body: string or None
        :return: Update a course
        :rtype: requests.Response (with void data)

    """

    payload = {
        'course[account_id]' : course_account_id,
        'course[name]' : course_name,
        'course[course_code]' : course_course_code,
        'course[start_at]' : course_start_at,
        'course[end_at]' : course_end_at,
        'course[license]' : course_license,
        'course[is_public]' : course_is_public,
        'course[is_public_to_auth_users]' : course_is_public_to_auth_users,
        'course[public_syllabus]' : course_public_syllabus,
        'course[public_description]' : course_public_description,
        'course[allow_student_wiki_edits]' : course_allow_student_wiki_edits,
        'course[allow_wiki_comments]' : course_allow_wiki_comments,
        'course[allow_student_forum_attachments]' : course_allow_student_forum_attachments,
        'course[open_enrollment]' : course_open_enrollment,
        'course[self_enrollment]' : course_self_enrollment,
        'course[restrict_enrollments_to_course_dates]' : course_restrict_enrollments_to_course_dates,
        'course[term_id]' : course_term_id,
        'course[sis_course_id]' : course_sis_course_id,
        'course[integration_id]' : course_integration_id,
        'course[hide_final_grades]' : course_hide_final_grades,
        'course[apply_assignment_group_weights]' : course_apply_assignment_group_weights,
        'offer' : offer,
        'course[syllabus_body]' : course_syllabus_body,
        'course[grading_standard_id]' : course_grading_standard_id,
        'course[course_format]' : course_course_format,
    }

    path = '/v1/courses/{id}'

    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response
