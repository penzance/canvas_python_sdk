from __future__ import unicode_literals
from canvas_sdk import client, utils

def create_assignment(request_ctx, course_id, assignment_name, assignment_submission_types, assignment_position=None, assignment_allowed_extensions=None, assignment_turnitin_enabled=None, assignment_integration_data=None, assignment_integration_id=None, assignment_turnitin_settings=None, assignment_peer_reviews=None, assignment_automatic_peer_reviews=None, assignment_notify_of_update=None, assignment_group_category_id=None, assignment_grade_group_students_individually=None, assignment_external_tool_tag_attributes=None, assignment_points_possible=None, assignment_grading_type=None, assignment_due_at=None, assignment_lock_at=None, assignment_unlock_at=None, assignment_description=None, assignment_assignment_group_id=None, assignment_muted=None, assignment_assignment_overrides=None, assignment_only_visible_to_overrides=None, assignment_published=None, assignment_grading_standard_id=None, **request_kwargs):
    """
    Create a new assignment for this course. The assignment is created in the
    active state.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_name: (required) The assignment name.
        :type assignment_name: string
        :param assignment_submission_types: (required) List of supported submission types for the assignment. Unless the assignment is allowing online submissions, the array should only have one element. If not allowing online submissions, your options are: "online_quiz" "none" "on_paper" "online_quiz" "discussion_topic" "external_tool" If you are allowing online submissions, you can have one or many allowed submission types: "online_upload" "online_text_entry" "online_url" "media_recording" (Only valid when the Kaltura plugin is enabled)
        :type assignment_submission_types: string
        :param assignment_position: (optional) The position of this assignment in the group when displaying assignment lists.
        :type assignment_position: integer or None
        :param assignment_allowed_extensions: (optional) Allowed extensions if submission_types includes "online_upload" Example: allowed_extensions: ["docx","ppt"]
        :type assignment_allowed_extensions: string or None
        :param assignment_turnitin_enabled: (optional) Only applies when the Turnitin plugin is enabled for a course and the submission_types array includes "online_upload". Toggles Turnitin submissions for the assignment. Will be ignored if Turnitin is not available for the course.
        :type assignment_turnitin_enabled: boolean or None
        :param assignment_integration_data: (optional) Data related to third party integrations, JSON string required.
        :type assignment_integration_data: string or None
        :param assignment_integration_id: (optional) Unique ID from third party integrations
        :type assignment_integration_id: string or None
        :param assignment_turnitin_settings: (optional) Settings to send along to turnitin. See Assignment object definition for format.
        :type assignment_turnitin_settings: string or None
        :param assignment_peer_reviews: (optional) If submission_types does not include external_tool,discussion_topic, online_quiz, or on_paper, determines whether or not peer reviews will be turned on for the assignment.
        :type assignment_peer_reviews: boolean or None
        :param assignment_automatic_peer_reviews: (optional) Whether peer reviews will be assigned automatically by Canvas or if teachers must manually assign peer reviews. Does not apply if peer reviews are not enabled.
        :type assignment_automatic_peer_reviews: boolean or None
        :param assignment_notify_of_update: (optional) If true, Canvas will send a notification to students in the class notifying them that the content has changed.
        :type assignment_notify_of_update: boolean or None
        :param assignment_group_category_id: (optional) If present, the assignment will become a group assignment assigned to the group.
        :type assignment_group_category_id: integer or None
        :param assignment_grade_group_students_individually: (optional) If this is a group assignment, teachers have the options to grade students individually. If false, Canvas will apply the assignment's score to each member of the group. If true, the teacher can manually assign scores to each member of the group.
        :type assignment_grade_group_students_individually: integer or None
        :param assignment_external_tool_tag_attributes: (optional) Hash of attributes if submission_types is ["external_tool"] Example: external_tool_tag_attributes: { // url to the external tool url: "http://instructure.com", // create a new tab for the module, defaults to false. new_tab: false }
        :type assignment_external_tool_tag_attributes: string or None
        :param assignment_points_possible: (optional) The maximum points possible on the assignment.
        :type assignment_points_possible: float or None
        :param assignment_grading_type: (optional) The strategy used for grading the assignment. The assignment is ungraded if this field is omitted.
        :type assignment_grading_type: string or None
        :param assignment_due_at: (optional) The day/time the assignment is due. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        :type assignment_due_at: timestamp or None
        :param assignment_lock_at: (optional) The day/time the assignment is locked after. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        :type assignment_lock_at: timestamp or None
        :param assignment_unlock_at: (optional) The day/time the assignment is unlocked. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        :type assignment_unlock_at: timestamp or None
        :param assignment_description: (optional) The assignment's description, supports HTML.
        :type assignment_description: string or None
        :param assignment_assignment_group_id: (optional) The assignment group id to put the assignment in. Defaults to the top assignment group in the course.
        :type assignment_assignment_group_id: integer or None
        :param assignment_muted: (optional) Whether this assignment is muted. A muted assignment does not send change notifications and hides grades from students. Defaults to false.
        :type assignment_muted: boolean or None
        :param assignment_assignment_overrides: (optional) List of overrides for the assignment. NOTE: The assignment overrides feature is in beta.
        :type assignment_assignment_overrides: assignmentoverride or None
        :param assignment_only_visible_to_overrides: (optional) Whether this assignment is only visible to overrides (Only useful if 'differentiated assignments' account setting is on)
        :type assignment_only_visible_to_overrides: boolean or None
        :param assignment_published: (optional) Whether this assignment is published. (Only useful if 'draft state' account setting is on) Unpublished assignments are not visible to students.
        :type assignment_published: boolean or None
        :param assignment_grading_standard_id: (optional) The grading standard id to set for the course. If no value is provided for this argument the current grading_standard will be un-set from this course. This will update the grading_type for the course to 'letter_grade' unless it is already 'gpa_scale'.
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
        'assignment[submission_types][]' : assignment_submission_types,
        'assignment[allowed_extensions]' : assignment_allowed_extensions,
        'assignment[turnitin_enabled]' : assignment_turnitin_enabled,
        'assignment[integration_data]' : assignment_integration_data,
        'assignment[integration_id]' : assignment_integration_id,
        'assignment[turnitin_settings]' : assignment_turnitin_settings,
        'assignment[peer_reviews]' : assignment_peer_reviews,
        'assignment[automatic_peer_reviews]' : assignment_automatic_peer_reviews,
        'assignment[notify_of_update]' : assignment_notify_of_update,
        'assignment[group_category_id]' : assignment_group_category_id,
        'assignment[grade_group_students_individually]' : assignment_grade_group_students_individually,
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
    for attribute, value in list((assignment_external_tool_tag_attributes or {}).items()):
        payload['assignment[external_tool_tag_attributes][{}]'.format(attribute)] = value
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def edit_assignment(request_ctx, course_id, id, assignment_name=None, assignment_position=None, assignment_submission_types=None, assignment_allowed_extensions=None, assignment_turnitin_enabled=None, assignment_turnitin_settings=None, assignment_peer_reviews=None, assignment_automatic_peer_reviews=None, assignment_notify_of_update=None, assignment_group_category_id=None, assignment_grade_group_students_individually=None, assignment_external_tool_tag_attributes=None, assignment_points_possible=None, assignment_grading_type=None, assignment_due_at=None, assignment_lock_at=None, assignment_unlock_at=None, assignment_description=None, assignment_assignment_group_id=None, assignment_muted=None, assignment_assignment_overrides=None, assignment_only_visible_to_overrides=None, assignment_published=None, assignment_grading_standard_id=None, **request_kwargs):
    """
    Modify an existing assignment.
    
    If the assignment[assignment_overrides] key is absent, any existing
    overrides are kept as is. If the assignment[assignment_overrides] key is
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
        :param assignment_position: (optional) The position of this assignment in the group when displaying assignment lists.
        :type assignment_position: integer or None
        :param assignment_submission_types: (optional) List of supported submission types for the assignment. Unless the assignment is allowing online submissions, the array should only have one element. If not allowing online submissions, your options are: "online_quiz" "none" "on_paper" "online_quiz" "discussion_topic" "external_tool" If you are allowing online submissions, you can have one or many allowed submission types: "online_upload" "online_text_entry" "online_url" "media_recording" (Only valid when the Kaltura plugin is enabled)
        :type assignment_submission_types: string or None
        :param assignment_allowed_extensions: (optional) Allowed extensions if submission_types includes "online_upload" Example: allowed_extensions: ["docx","ppt"]
        :type assignment_allowed_extensions: string or None
        :param assignment_turnitin_enabled: (optional) Only applies when the Turnitin plugin is enabled for a course and the submission_types array includes "online_upload". Toggles Turnitin submissions for the assignment. Will be ignored if Turnitin is not available for the course.
        :type assignment_turnitin_enabled: boolean or None
        :param assignment_turnitin_settings: (optional) Settings to send along to turnitin. See Assignment object definition for format.
        :type assignment_turnitin_settings: string or None
        :param assignment_peer_reviews: (optional) If submission_types does not include external_tool,discussion_topic, online_quiz, or on_paper, determines whether or not peer reviews will be turned on for the assignment.
        :type assignment_peer_reviews: boolean or None
        :param assignment_automatic_peer_reviews: (optional) Whether peer reviews will be assigned automatically by Canvas or if teachers must manually assign peer reviews. Does not apply if peer reviews are not enabled.
        :type assignment_automatic_peer_reviews: boolean or None
        :param assignment_notify_of_update: (optional) If true, Canvas will send a notification to students in the class notifying them that the content has changed.
        :type assignment_notify_of_update: boolean or None
        :param assignment_group_category_id: (optional) If present, the assignment will become a group assignment assigned to the group.
        :type assignment_group_category_id: integer or None
        :param assignment_grade_group_students_individually: (optional) If this is a group assignment, teachers have the options to grade students individually. If false, Canvas will apply the assignment's score to each member of the group. If true, the teacher can manually assign scores to each member of the group.
        :type assignment_grade_group_students_individually: integer or None
        :param assignment_external_tool_tag_attributes: (optional) Hash of attributes if submission_types is ["external_tool"] Example: external_tool_tag_attributes: { // url to the external tool url: "http://instructure.com", // create a new tab for the module, defaults to false. new_tab: false }
        :type assignment_external_tool_tag_attributes: string or None
        :param assignment_points_possible: (optional) The maximum points possible on the assignment.
        :type assignment_points_possible: float or None
        :param assignment_grading_type: (optional) The strategy used for grading the assignment. The assignment is ungraded if this field is omitted.
        :type assignment_grading_type: string or None
        :param assignment_due_at: (optional) The day/time the assignment is due. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        :type assignment_due_at: timestamp or None
        :param assignment_lock_at: (optional) The day/time the assignment is locked after. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        :type assignment_lock_at: timestamp or None
        :param assignment_unlock_at: (optional) The day/time the assignment is unlocked. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        :type assignment_unlock_at: timestamp or None
        :param assignment_description: (optional) The assignment's description, supports HTML.
        :type assignment_description: string or None
        :param assignment_assignment_group_id: (optional) The assignment group id to put the assignment in. Defaults to the top assignment group in the course.
        :type assignment_assignment_group_id: integer or None
        :param assignment_muted: (optional) Whether this assignment is muted. A muted assignment does not send change notifications and hides grades from students. Defaults to false.
        :type assignment_muted: boolean or None
        :param assignment_assignment_overrides: (optional) List of overrides for the assignment. NOTE: The assignment overrides feature is in beta.
        :type assignment_assignment_overrides: assignmentoverride or None
        :param assignment_only_visible_to_overrides: (optional) Whether this assignment is only visible to overrides (Only useful if 'differentiated assignments' account setting is on)
        :type assignment_only_visible_to_overrides: boolean or None
        :param assignment_published: (optional) Whether this assignment is published. (Only useful if 'draft state' account setting is on) Unpublished assignments are not visible to students.
        :type assignment_published: boolean or None
        :param assignment_grading_standard_id: (optional) The grading standard id to set for the course. If no value is provided for this argument the current grading_standard will be un-set from this course. This will update the grading_type for the course to 'letter_grade' unless it is already 'gpa_scale'.
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
        'assignment[submission_types][]' : assignment_submission_types,
        'assignment[allowed_extensions]' : assignment_allowed_extensions,
        'assignment[turnitin_enabled]' : assignment_turnitin_enabled,
        'assignment[turnitin_settings]' : assignment_turnitin_settings,
        'assignment[peer_reviews]' : assignment_peer_reviews,
        'assignment[automatic_peer_reviews]' : assignment_automatic_peer_reviews,
        'assignment[notify_of_update]' : assignment_notify_of_update,
        'assignment[group_category_id]' : assignment_group_category_id,
        'assignment[grade_group_students_individually]' : assignment_grade_group_students_individually,
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
    for attribute, value in list((assignment_external_tool_tag_attributes or {}).items()):
        payload['assignment[external_tool_tag_attributes][{}]'.format(attribute)] = value
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response
