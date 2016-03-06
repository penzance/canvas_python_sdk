from canvas_sdk import client, utils

def delete_assignment(request_ctx, course_id, id, **request_kwargs):
    """
    Delete the given assignment.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete an assignment
        :rtype: requests.Response (with Assignment data)

    """

    path = '/v1/courses/{course_id}/assignments/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def list_assignments(request_ctx, course_id, include=None, search_term=None, override_assignment_dates=None, needs_grading_count_by_section=None, bucket=None, per_page=None, **request_kwargs):
    """
    Returns the list of assignments for the current context.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param include: (optional) Associations to include with the assignment. The "assignment_visibility" option
requires that the Differentiated Assignments course feature be turned on. If
"observed_users" is passed, submissions for observed users will also be included as an array.
        :type include: array or None
        :param search_term: (optional) The partial title of the assignments to match and return.
        :type search_term: string or None
        :param override_assignment_dates: (optional) Apply assignment overrides for each assignment, defaults to true.
        :type override_assignment_dates: boolean or None
        :param needs_grading_count_by_section: (optional) Split up "needs_grading_count" by sections into the "needs_grading_count_by_section" key, defaults to false
        :type needs_grading_count_by_section: boolean or None
        :param bucket: (optional) If included, only return certain assignments depending on due date and submission status.
        :type bucket: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List assignments
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('submission', 'assignment_visibility', 'all_dates', 'overrides', 'observed_users')
    bucket_types = ('past', 'overdue', 'undated', 'ungraded', 'upcoming', 'future')
    utils.validate_attr_is_acceptable(include, include_types)
    utils.validate_attr_is_acceptable(bucket, bucket_types)
    path = '/v1/courses/{course_id}/assignments'
    payload = {
        'include' : include,
        'search_term' : search_term,
        'override_assignment_dates' : override_assignment_dates,
        'needs_grading_count_by_section' : needs_grading_count_by_section,
        'bucket' : bucket,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_assignments_for_user(request_ctx, user_id, course_id, per_page=None, **request_kwargs):
    """
    Returns the list of assignments for the specified user if the current user has rights to view.
    See `AssignmentsApiController#index <https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignments_api_controller.rb>`_ for valid arguments.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List assignments for user
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/courses/{course_id}/assignments'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id, course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_assignment(request_ctx, course_id, id, include=None, override_assignment_dates=None, needs_grading_count_by_section=None, all_dates=None, **request_kwargs):
    """
    Returns the assignment with the given id.
     "observed_users" is passed, submissions for observed users will also be included.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param include: (optional) Associations to include with the assignment. The "assignment_visibility" option
requires that the Differentiated Assignments course feature be turned on. If
        :type include: array or None
        :param override_assignment_dates: (optional) Apply assignment overrides to the assignment, defaults to true.
        :type override_assignment_dates: boolean or None
        :param needs_grading_count_by_section: (optional) Split up "needs_grading_count" by sections into the "needs_grading_count_by_section" key, defaults to false
        :type needs_grading_count_by_section: boolean or None
        :param all_dates: (optional) All dates associated with the assignment, if applicable
        :type all_dates: boolean or None
        :return: Get a single assignment
        :rtype: requests.Response (with Assignment data)

    """

    include_types = ('submission', 'assignment_visibility', 'overrides', 'observed_users')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/assignments/{id}'
    payload = {
        'include' : include,
        'override_assignment_dates' : override_assignment_dates,
        'needs_grading_count_by_section' : needs_grading_count_by_section,
        'all_dates' : all_dates,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_assignment(request_ctx, course_id, assignment_name, assignment_position=None, assignment_submission_types=None, assignment_allowed_extensions=None, assignment_turnitin_enabled=None, assignment_turnitin_settings=None, assignment_integration_data=None, assignment_integration_id=None, assignment_peer_reviews=None, assignment_automatic_peer_reviews=None, assignment_notify_of_update=None, assignment_group_category_id=None, assignment_grade_group_students_individually=None, assignment_external_tool_tag_attributes=None, assignment_points_possible=None, assignment_grading_type=None, assignment_due_at=None, assignment_lock_at=None, assignment_unlock_at=None, assignment_description=None, assignment_assignment_group_id=None, assignment_muted=None, assignment_assignment_overrides=None, assignment_only_visible_to_overrides=None, assignment_published=None, assignment_grading_standard_id=None, **request_kwargs):
    """
    Create a new assignment for this course. The assignment is created in the
    active state.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_name: (required) The assignment name.
        :type assignment_name: string
        :param assignment_position: (optional) The position of this assignment in the group when displaying
assignment lists.
        :type assignment_position: integer or None
        :param assignment_submission_types: (optional) List of supported submission types for the assignment.
Unless the assignment is allowing online submissions, the array should
only have one element.

If not allowing online submissions, your options are:
  "online_quiz"
  "none"
  "on_paper"
  "online_quiz"
  "discussion_topic"
  "external_tool"

If you are allowing online submissions, you can have one or many
allowed submission types:

  "online_upload"
  "online_text_entry"
  "online_url"
  "media_recording" (Only valid when the Kaltura plugin is enabled)
        :type assignment_submission_types: array or None
        :param assignment_allowed_extensions: (optional) Allowed extensions if submission_types includes "online_upload"

Example:
  allowed_extensions: ["docx","ppt"]
        :type assignment_allowed_extensions: array or None
        :param assignment_turnitin_enabled: (optional) Only applies when the Turnitin plugin is enabled for a course and
the submission_types array includes "online_upload".
Toggles Turnitin submissions for the assignment.
Will be ignored if Turnitin is not available for the course.
        :type assignment_turnitin_enabled: boolean or None
        :param assignment_turnitin_settings: (optional) Settings to send along to turnitin. See Assignment object definition for
format.
        :type assignment_turnitin_settings: string or None
        :param assignment_integration_data: (optional) Data related to third party integrations, JSON string required.
        :type assignment_integration_data: string or None
        :param assignment_integration_id: (optional) Unique ID from third party integrations
        :type assignment_integration_id: string or None
        :param assignment_peer_reviews: (optional) If submission_types does not include external_tool,discussion_topic,
online_quiz, or on_paper, determines whether or not peer reviews
will be turned on for the assignment.
        :type assignment_peer_reviews: boolean or None
        :param assignment_automatic_peer_reviews: (optional) Whether peer reviews will be assigned automatically by Canvas or if
teachers must manually assign peer reviews. Does not apply if peer reviews
are not enabled.
        :type assignment_automatic_peer_reviews: boolean or None
        :param assignment_notify_of_update: (optional) If true, Canvas will send a notification to students in the class
notifying them that the content has changed.
        :type assignment_notify_of_update: boolean or None
        :param assignment_group_category_id: (optional) If present, the assignment will become a group assignment assigned
to the group.
        :type assignment_group_category_id: integer or None
        :param assignment_grade_group_students_individually: (optional) If this is a group assignment, teachers have the options to grade
students individually. If false, Canvas will apply the assignment's
score to each member of the group. If true, the teacher can manually
assign scores to each member of the group.
        :type assignment_grade_group_students_individually: integer or None
        :param assignment_external_tool_tag_attributes: (optional) Hash of attributes if submission_types is ["external_tool"]
Example:
  external_tool_tag_attributes: {
    // url to the external tool
    url: "http://instructure.com",
    // create a new tab for the module, defaults to false.
    new_tab: false
  }
        :type assignment_external_tool_tag_attributes: string or None
        :param assignment_points_possible: (optional) The maximum points possible on the assignment.
        :type assignment_points_possible: Float or None
        :param assignment_grading_type: (optional) The strategy used for grading the assignment.
The assignment is ungraded if this field is omitted.
        :type assignment_grading_type: string or None
        :param assignment_due_at: (optional) The day/time the assignment is due.
Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        :type assignment_due_at: DateTime or None
        :param assignment_lock_at: (optional) The day/time the assignment is locked after.
Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        :type assignment_lock_at: DateTime or None
        :param assignment_unlock_at: (optional) The day/time the assignment is unlocked.
Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        :type assignment_unlock_at: DateTime or None
        :param assignment_description: (optional) The assignment's description, supports HTML.
        :type assignment_description: string or None
        :param assignment_assignment_group_id: (optional) The assignment group id to put the assignment in.
Defaults to the top assignment group in the course.
        :type assignment_assignment_group_id: integer or None
        :param assignment_muted: (optional) Whether this assignment is muted.
A muted assignment does not send change notifications
and hides grades from students.
Defaults to false.
        :type assignment_muted: boolean or None
        :param assignment_assignment_overrides: (optional) List of overrides for the assignment.
NOTE: The assignment overrides feature is in beta.
        :type assignment_assignment_overrides: array or None
        :param assignment_only_visible_to_overrides: (optional) Whether this assignment is only visible to overrides
(Only useful if 'differentiated assignments' account setting is on)
        :type assignment_only_visible_to_overrides: boolean or None
        :param assignment_published: (optional) Whether this assignment is published.
(Only useful if 'draft state' account setting is on)
Unpublished assignments are not visible to students.
        :type assignment_published: boolean or None
        :param assignment_grading_standard_id: (optional) The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course.
This will update the grading_type for the course to 'letter_grade' unless it is already 'gpa_scale'.
        :type assignment_grading_standard_id: integer or None
        :return: Create an assignment
        :rtype: requests.Response (with Assignment data)

    """

    assignment_submission_types_types = ('online_quiz', 'none', 'on_paper', 'online_quiz', 'discussion_topic', 'external_tool', 'online_upload', 'online_text_entry', 'online_url', 'media_recording')
    assignment_grading_type_types = ('pass_fail', 'percent', 'letter_grade', 'gpa_scale', 'points')
    utils.validate_attr_is_acceptable(assignment_submission_types, assignment_submission_types_types)
    utils.validate_attr_is_acceptable(assignment_grading_type, assignment_grading_type_types)
    path = '/v1/courses/{course_id}/assignments'
    payload = {
        'assignment[name]' : assignment_name,
        'assignment[position]' : assignment_position,
        'assignment[submission_types]' : assignment_submission_types,
        'assignment[allowed_extensions]' : assignment_allowed_extensions,
        'assignment[turnitin_enabled]' : assignment_turnitin_enabled,
        'assignment[turnitin_settings]' : assignment_turnitin_settings,
        'assignment[integration_data]' : assignment_integration_data,
        'assignment[integration_id]' : assignment_integration_id,
        'assignment[peer_reviews]' : assignment_peer_reviews,
        'assignment[automatic_peer_reviews]' : assignment_automatic_peer_reviews,
        'assignment[notify_of_update]' : assignment_notify_of_update,
        'assignment[group_category_id]' : assignment_group_category_id,
        'assignment[grade_group_students_individually]' : assignment_grade_group_students_individually,
        'assignment[external_tool_tag_attributes]' : assignment_external_tool_tag_attributes,
        'assignment[points_possible]' : assignment_points_possible,
        'assignment[grading_type]' : assignment_grading_type,
        'assignment[due_at]' : assignment_due_at,
        'assignment[lock_at]' : assignment_lock_at,
        'assignment[unlock_at]' : assignment_unlock_at,
        'assignment[description]' : assignment_description,
        'assignment[assignment_group_id]' : assignment_assignment_group_id,
        'assignment[muted]' : assignment_muted,
        'assignment[assignment_overrides]' : assignment_assignment_overrides,
        'assignment[only_visible_to_overrides]' : assignment_only_visible_to_overrides,
        'assignment[published]' : assignment_published,
        'assignment[grading_standard_id]' : assignment_grading_standard_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def edit_assignment(request_ctx, course_id, id, assignment_name=None, assignment_position=None, assignment_submission_types=None, assignment_allowed_extensions=None, assignment_turnitin_enabled=None, assignment_turnitin_settings=None, assignment_integration_data=None, assignment_integration_id=None, assignment_peer_reviews=None, assignment_automatic_peer_reviews=None, assignment_notify_of_update=None, assignment_group_category_id=None, assignment_grade_group_students_individually=None, assignment_external_tool_tag_attributes=None, assignment_points_possible=None, assignment_grading_type=None, assignment_due_at=None, assignment_lock_at=None, assignment_unlock_at=None, assignment_description=None, assignment_assignment_group_id=None, assignment_muted=None, assignment_assignment_overrides=None, assignment_only_visible_to_overrides=None, assignment_published=None, assignment_grading_standard_id=None, **request_kwargs):
    """
    Modify an existing assignment.
    
    If the assignment [assignment_overrides] key is absent, any existing
    overrides are kept as is. If the assignment [assignment_overrides] key is
    present, existing overrides are updated or deleted (and new ones created,
    as necessary) to match the provided list.
    
    NOTE: The assignment overrides feature is in beta.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param assignment_name: (optional) The assignment name.
        :type assignment_name: string or None
        :param assignment_position: (optional) The position of this assignment in the group when displaying
assignment lists.
        :type assignment_position: integer or None
        :param assignment_submission_types: (optional) List of supported submission types for the assignment.
Unless the assignment is allowing online submissions, the array should
only have one element.

If not allowing online submissions, your options are:
  "online_quiz"
  "none"
  "on_paper"
  "online_quiz"
  "discussion_topic"
  "external_tool"

If you are allowing online submissions, you can have one or many
allowed submission types:

  "online_upload"
  "online_text_entry"
  "online_url"
  "media_recording" (Only valid when the Kaltura plugin is enabled)
        :type assignment_submission_types: array or None
        :param assignment_allowed_extensions: (optional) Allowed extensions if submission_types includes "online_upload"

Example:
  allowed_extensions: ["docx","ppt"]
        :type assignment_allowed_extensions: array or None
        :param assignment_turnitin_enabled: (optional) Only applies when the Turnitin plugin is enabled for a course and
the submission_types array includes "online_upload".
Toggles Turnitin submissions for the assignment.
Will be ignored if Turnitin is not available for the course.
        :type assignment_turnitin_enabled: boolean or None
        :param assignment_turnitin_settings: (optional) Settings to send along to turnitin. See Assignment object definition for
format.
        :type assignment_turnitin_settings: string or None
        :param assignment_integration_data: (optional) Data related to third party integrations, JSON string required.
        :type assignment_integration_data: string or None
        :param assignment_integration_id: (optional) Unique ID from third party integrations
        :type assignment_integration_id: string or None
        :param assignment_peer_reviews: (optional) If submission_types does not include external_tool,discussion_topic,
online_quiz, or on_paper, determines whether or not peer reviews
will be turned on for the assignment.
        :type assignment_peer_reviews: boolean or None
        :param assignment_automatic_peer_reviews: (optional) Whether peer reviews will be assigned automatically by Canvas or if
teachers must manually assign peer reviews. Does not apply if peer reviews
are not enabled.
        :type assignment_automatic_peer_reviews: boolean or None
        :param assignment_notify_of_update: (optional) If true, Canvas will send a notification to students in the class
notifying them that the content has changed.
        :type assignment_notify_of_update: boolean or None
        :param assignment_group_category_id: (optional) If present, the assignment will become a group assignment assigned
to the group.
        :type assignment_group_category_id: integer or None
        :param assignment_grade_group_students_individually: (optional) If this is a group assignment, teachers have the options to grade
students individually. If false, Canvas will apply the assignment's
score to each member of the group. If true, the teacher can manually
assign scores to each member of the group.
        :type assignment_grade_group_students_individually: integer or None
        :param assignment_external_tool_tag_attributes: (optional) Hash of attributes if submission_types is ["external_tool"]
Example:
  external_tool_tag_attributes: {
    // url to the external tool
    url: "http://instructure.com",
    // create a new tab for the module, defaults to false.
    new_tab: false
  }
        :type assignment_external_tool_tag_attributes: string or None
        :param assignment_points_possible: (optional) The maximum points possible on the assignment.
        :type assignment_points_possible: Float or None
        :param assignment_grading_type: (optional) The strategy used for grading the assignment.
The assignment is ungraded if this field is omitted.
        :type assignment_grading_type: string or None
        :param assignment_due_at: (optional) The day/time the assignment is due.
Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        :type assignment_due_at: DateTime or None
        :param assignment_lock_at: (optional) The day/time the assignment is locked after.
Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        :type assignment_lock_at: DateTime or None
        :param assignment_unlock_at: (optional) The day/time the assignment is unlocked.
Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        :type assignment_unlock_at: DateTime or None
        :param assignment_description: (optional) The assignment's description, supports HTML.
        :type assignment_description: string or None
        :param assignment_assignment_group_id: (optional) The assignment group id to put the assignment in.
Defaults to the top assignment group in the course.
        :type assignment_assignment_group_id: integer or None
        :param assignment_muted: (optional) Whether this assignment is muted.
A muted assignment does not send change notifications
and hides grades from students.
Defaults to false.
        :type assignment_muted: boolean or None
        :param assignment_assignment_overrides: (optional) List of overrides for the assignment.
NOTE: The assignment overrides feature is in beta.
        :type assignment_assignment_overrides: array or None
        :param assignment_only_visible_to_overrides: (optional) Whether this assignment is only visible to overrides
(Only useful if 'differentiated assignments' account setting is on)
        :type assignment_only_visible_to_overrides: boolean or None
        :param assignment_published: (optional) Whether this assignment is published.
(Only useful if 'draft state' account setting is on)
Unpublished assignments are not visible to students.
        :type assignment_published: boolean or None
        :param assignment_grading_standard_id: (optional) The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course.
This will update the grading_type for the course to 'letter_grade' unless it is already 'gpa_scale'.
        :type assignment_grading_standard_id: integer or None
        :return: Edit an assignment
        :rtype: requests.Response (with Assignment data)

    """

    assignment_submission_types_types = ('online_quiz', 'none', 'on_paper', 'online_quiz', 'discussion_topic', 'external_tool', 'online_upload', 'online_text_entry', 'online_url', 'media_recording')
    assignment_grading_type_types = ('pass_fail', 'percent', 'letter_grade', 'gpa_scale', 'points')
    utils.validate_attr_is_acceptable(assignment_submission_types, assignment_submission_types_types)
    utils.validate_attr_is_acceptable(assignment_grading_type, assignment_grading_type_types)
    path = '/v1/courses/{course_id}/assignments/{id}'
    payload = {
        'assignment[name]' : assignment_name,
        'assignment[position]' : assignment_position,
        'assignment[submission_types]' : assignment_submission_types,
        'assignment[allowed_extensions]' : assignment_allowed_extensions,
        'assignment[turnitin_enabled]' : assignment_turnitin_enabled,
        'assignment[turnitin_settings]' : assignment_turnitin_settings,
        'assignment[integration_data]' : assignment_integration_data,
        'assignment[integration_id]' : assignment_integration_id,
        'assignment[peer_reviews]' : assignment_peer_reviews,
        'assignment[automatic_peer_reviews]' : assignment_automatic_peer_reviews,
        'assignment[notify_of_update]' : assignment_notify_of_update,
        'assignment[group_category_id]' : assignment_group_category_id,
        'assignment[grade_group_students_individually]' : assignment_grade_group_students_individually,
        'assignment[external_tool_tag_attributes]' : assignment_external_tool_tag_attributes,
        'assignment[points_possible]' : assignment_points_possible,
        'assignment[grading_type]' : assignment_grading_type,
        'assignment[due_at]' : assignment_due_at,
        'assignment[lock_at]' : assignment_lock_at,
        'assignment[unlock_at]' : assignment_unlock_at,
        'assignment[description]' : assignment_description,
        'assignment[assignment_group_id]' : assignment_assignment_group_id,
        'assignment[muted]' : assignment_muted,
        'assignment[assignment_overrides]' : assignment_assignment_overrides,
        'assignment[only_visible_to_overrides]' : assignment_only_visible_to_overrides,
        'assignment[published]' : assignment_published,
        'assignment[grading_standard_id]' : assignment_grading_standard_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_assignment_overrides(request_ctx, course_id, assignment_id, per_page=None, **request_kwargs):
    """
    Returns the list of overrides for this assignment that target
    sections/groups/students visible to the current user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List assignment overrides
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/assignments/{assignment_id}/overrides'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_assignment_override(request_ctx, course_id, assignment_id, id, **request_kwargs):
    """
    Returns details of the the override with the given id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param id: (required) ID
        :type id: string
        :return: Get a single assignment override
        :rtype: requests.Response (with AssignmentOverride data)

    """

    path = '/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def redirect_to_assignment_override_for_group(request_ctx, group_id, assignment_id, **request_kwargs):
    """
    Responds with a redirect to the override for the given group, if any
    (404 otherwise).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :return: Redirect to the assignment override for a group
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/assignments/{assignment_id}/override'
    url = request_ctx.base_api_url + path.format(group_id=group_id, assignment_id=assignment_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def redirect_to_assignment_override_for_section(request_ctx, course_section_id, assignment_id, **request_kwargs):
    """
    Responds with a redirect to the override for the given section, if any
    (404 otherwise).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_section_id: (required) ID
        :type course_section_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :return: Redirect to the assignment override for a section
        :rtype: requests.Response (with void data)

    """

    path = '/v1/sections/{course_section_id}/assignments/{assignment_id}/override'
    url = request_ctx.base_api_url + path.format(course_section_id=course_section_id, assignment_id=assignment_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_assignment_override(request_ctx, course_id, assignment_id, assignment_override_student_ids=None, assignment_override_title=None, assignment_override_group_id=None, assignment_override_course_section_id=None, assignment_override_due_at=None, assignment_override_unlock_at=None, assignment_override_lock_at=None, **request_kwargs):
    """
    One of student_ids, group_id, or course_section_id must be present. At most
    one should be present; if multiple are present only the most specific
    (student_ids first, then group_id, then course_section_id) is used and any
    others are ignored.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param assignment_override_student_ids: (optional) The IDs of
the override's target students. If present, the IDs must each identify a
user with an active student enrollment in the course that is not already
targetted by a different adhoc override.
        :type assignment_override_student_ids: array or None
        :param assignment_override_title: (optional) The title of the adhoc
assignment override. Required if student_ids is present, ignored
otherwise (the title is set to the name of the targetted group or section
instead).
        :type assignment_override_title: string or None
        :param assignment_override_group_id: (optional) The ID of the
override's target group. If present, the following conditions must be met
for the override to be successful:

1. the assignment MUST be a group assignment (a group_category_id is assigned to it)
2. the ID must identify an active group in the group set the assignment is in
3. the ID must not be targetted by a different override

See {Appendix: Group assignments} for more info.
        :type assignment_override_group_id: integer or None
        :param assignment_override_course_section_id: (optional) The ID
of the override's target section. If present, must identify an active
section of the assignment's course not already targetted by a different
override.
        :type assignment_override_course_section_id: integer or None
        :param assignment_override_due_at: (optional) The day/time
the overridden assignment is due. Accepts times in ISO 8601 format, e.g.
2014-10-21T18:48:00Z. If absent, this override will not affect due date.
May be present but null to indicate the override removes any previous due
date.
        :type assignment_override_due_at: DateTime or None
        :param assignment_override_unlock_at: (optional) The day/time
the overridden assignment becomes unlocked. Accepts times in ISO 8601
format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not
affect the unlock date. May be present but null to indicate the override
removes any previous unlock date.
        :type assignment_override_unlock_at: DateTime or None
        :param assignment_override_lock_at: (optional) The day/time
the overridden assignment becomes locked. Accepts times in ISO 8601
format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not
affect the lock date. May be present but null to indicate the override
removes any previous lock date.
        :type assignment_override_lock_at: DateTime or None
        :return: Create an assignment override
        :rtype: requests.Response (with AssignmentOverride data)

    """

    path = '/v1/courses/{course_id}/assignments/{assignment_id}/overrides'
    payload = {
        'assignment_override[student_ids]' : assignment_override_student_ids,
        'assignment_override[title]' : assignment_override_title,
        'assignment_override[group_id]' : assignment_override_group_id,
        'assignment_override[course_section_id]' : assignment_override_course_section_id,
        'assignment_override[due_at]' : assignment_override_due_at,
        'assignment_override[unlock_at]' : assignment_override_unlock_at,
        'assignment_override[lock_at]' : assignment_override_lock_at,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_assignment_override(request_ctx, course_id, assignment_id, id, assignment_override_student_ids=None, assignment_override_title=None, assignment_override_due_at=None, assignment_override_unlock_at=None, assignment_override_lock_at=None, **request_kwargs):
    """
    All current overridden values must be supplied if they are to be retained;
    e.g. if due_at was overridden, but this PUT omits a value for due_at,
    due_at will no longer be overridden. If the override is adhoc and
    student_ids is not supplied, the target override set is unchanged. Target
    override sets cannot be changed for group or section overrides.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param id: (required) ID
        :type id: string
        :param assignment_override_student_ids: (optional) The IDs of the
override's target students. If present, the IDs must each identify a
user with an active student enrollment in the course that is not already
targetted by a different adhoc override. Ignored unless the override
being updated is adhoc.
        :type assignment_override_student_ids: array or None
        :param assignment_override_title: (optional) The title of an adhoc
assignment override. Ignored unless the override being updated is adhoc.
        :type assignment_override_title: string or None
        :param assignment_override_due_at: (optional) The day/time
the overridden assignment is due. Accepts times in ISO 8601 format, e.g.
2014-10-21T18:48:00Z. If absent, this override will not affect due date.
May be present but null to indicate the override removes any previous due
date.
        :type assignment_override_due_at: DateTime or None
        :param assignment_override_unlock_at: (optional) The day/time
the overridden assignment becomes unlocked. Accepts times in ISO 8601
format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not
affect the unlock date. May be present but null to indicate the override
removes any previous unlock date.
        :type assignment_override_unlock_at: DateTime or None
        :param assignment_override_lock_at: (optional) The day/time
the overridden assignment becomes locked. Accepts times in ISO 8601
format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not
affect the lock date. May be present but null to indicate the override
removes any previous lock date.
        :type assignment_override_lock_at: DateTime or None
        :return: Update an assignment override
        :rtype: requests.Response (with AssignmentOverride data)

    """

    path = '/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}'
    payload = {
        'assignment_override[student_ids]' : assignment_override_student_ids,
        'assignment_override[title]' : assignment_override_title,
        'assignment_override[due_at]' : assignment_override_due_at,
        'assignment_override[unlock_at]' : assignment_override_unlock_at,
        'assignment_override[lock_at]' : assignment_override_lock_at,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_assignment_override(request_ctx, course_id, assignment_id, id, **request_kwargs):
    """
    Deletes an override and returns its former details.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete an assignment override
        :rtype: requests.Response (with AssignmentOverride data)

    """

    path = '/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


