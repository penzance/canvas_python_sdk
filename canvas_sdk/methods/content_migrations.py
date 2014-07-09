from canvas_sdk import client, utils

def list_migration_issues_accounts(request_ctx, account_id, content_migration_id, per_page=None, **request_kwargs):
    """
    Returns paginated migration issues

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param content_migration_id: (required) ID
        :type content_migration_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List migration issues
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, content_migration_id=content_migration_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_migration_issues_courses(request_ctx, course_id, content_migration_id, per_page=None, **request_kwargs):
    """
    Returns paginated migration issues

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param content_migration_id: (required) ID
        :type content_migration_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List migration issues
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, content_migration_id=content_migration_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_migration_issues_groups(request_ctx, group_id, content_migration_id, per_page=None, **request_kwargs):
    """
    Returns paginated migration issues

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param content_migration_id: (required) ID
        :type content_migration_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List migration issues
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, content_migration_id=content_migration_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_migration_issues_users(request_ctx, user_id, content_migration_id, per_page=None, **request_kwargs):
    """
    Returns paginated migration issues

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param content_migration_id: (required) ID
        :type content_migration_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List migration issues
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id, content_migration_id=content_migration_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_migration_issue_accounts(request_ctx, account_id, content_migration_id, id, **request_kwargs):
    """
    Returns data on an individual migration issue

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param content_migration_id: (required) ID
        :type content_migration_id: string
        :param id: (required) ID
        :type id: string
        :return: Get a migration issue
        :rtype: requests.Response (with MigrationIssue data)

    """

    path = '/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, content_migration_id=content_migration_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_migration_issue_courses(request_ctx, course_id, content_migration_id, id, **request_kwargs):
    """
    Returns data on an individual migration issue

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param content_migration_id: (required) ID
        :type content_migration_id: string
        :param id: (required) ID
        :type id: string
        :return: Get a migration issue
        :rtype: requests.Response (with MigrationIssue data)

    """

    path = '/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, content_migration_id=content_migration_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_migration_issue_groups(request_ctx, group_id, content_migration_id, id, **request_kwargs):
    """
    Returns data on an individual migration issue

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param content_migration_id: (required) ID
        :type content_migration_id: string
        :param id: (required) ID
        :type id: string
        :return: Get a migration issue
        :rtype: requests.Response (with MigrationIssue data)

    """

    path = '/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, content_migration_id=content_migration_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_migration_issue_users(request_ctx, user_id, content_migration_id, id, **request_kwargs):
    """
    Returns data on an individual migration issue

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param content_migration_id: (required) ID
        :type content_migration_id: string
        :param id: (required) ID
        :type id: string
        :return: Get a migration issue
        :rtype: requests.Response (with MigrationIssue data)

    """

    path = '/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, content_migration_id=content_migration_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def update_migration_issue_accounts(request_ctx, account_id, content_migration_id, id, workflow_state, **request_kwargs):
    """
    Update the workflow_state of a migration issue

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param content_migration_id: (required) ID
        :type content_migration_id: string
        :param id: (required) ID
        :type id: string
        :param workflow_state: (required) Set the workflow_state of the issue.
        :type workflow_state: string
        :return: Update a migration issue
        :rtype: requests.Response (with MigrationIssue data)

    """

    workflow_state_types = ('active', 'resolved')
    utils.validate_attr_is_acceptable(workflow_state, workflow_state_types)
    path = '/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id}'
    payload = {
        'workflow_state' : workflow_state,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, content_migration_id=content_migration_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_migration_issue_courses(request_ctx, course_id, content_migration_id, id, workflow_state, **request_kwargs):
    """
    Update the workflow_state of a migration issue

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param content_migration_id: (required) ID
        :type content_migration_id: string
        :param id: (required) ID
        :type id: string
        :param workflow_state: (required) Set the workflow_state of the issue.
        :type workflow_state: string
        :return: Update a migration issue
        :rtype: requests.Response (with MigrationIssue data)

    """

    workflow_state_types = ('active', 'resolved')
    utils.validate_attr_is_acceptable(workflow_state, workflow_state_types)
    path = '/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id}'
    payload = {
        'workflow_state' : workflow_state,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, content_migration_id=content_migration_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_migration_issue_groups(request_ctx, group_id, content_migration_id, id, workflow_state, **request_kwargs):
    """
    Update the workflow_state of a migration issue

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param content_migration_id: (required) ID
        :type content_migration_id: string
        :param id: (required) ID
        :type id: string
        :param workflow_state: (required) Set the workflow_state of the issue.
        :type workflow_state: string
        :return: Update a migration issue
        :rtype: requests.Response (with MigrationIssue data)

    """

    workflow_state_types = ('active', 'resolved')
    utils.validate_attr_is_acceptable(workflow_state, workflow_state_types)
    path = '/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id}'
    payload = {
        'workflow_state' : workflow_state,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, content_migration_id=content_migration_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_migration_issue_users(request_ctx, user_id, content_migration_id, id, workflow_state, **request_kwargs):
    """
    Update the workflow_state of a migration issue

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param content_migration_id: (required) ID
        :type content_migration_id: string
        :param id: (required) ID
        :type id: string
        :param workflow_state: (required) Set the workflow_state of the issue.
        :type workflow_state: string
        :return: Update a migration issue
        :rtype: requests.Response (with MigrationIssue data)

    """

    workflow_state_types = ('active', 'resolved')
    utils.validate_attr_is_acceptable(workflow_state, workflow_state_types)
    path = '/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id}'
    payload = {
        'workflow_state' : workflow_state,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id, content_migration_id=content_migration_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_content_migrations_accounts(request_ctx, account_id, per_page=None, **request_kwargs):
    """
    Returns paginated content migrations

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List content migrations
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/content_migrations'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_content_migrations_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Returns paginated content migrations

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List content migrations
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/content_migrations'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_content_migrations_groups(request_ctx, group_id, per_page=None, **request_kwargs):
    """
    Returns paginated content migrations

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List content migrations
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/groups/{group_id}/content_migrations'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_content_migrations_users(request_ctx, user_id, per_page=None, **request_kwargs):
    """
    Returns paginated content migrations

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List content migrations
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/content_migrations'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_content_migration_accounts(request_ctx, account_id, id, **request_kwargs):
    """
    Returns data on an individual content migration

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Get a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/accounts/{account_id}/content_migrations/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_content_migration_courses(request_ctx, course_id, id, **request_kwargs):
    """
    Returns data on an individual content migration

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Get a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/courses/{course_id}/content_migrations/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_content_migration_groups(request_ctx, group_id, id, **request_kwargs):
    """
    Returns data on an individual content migration

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param id: (required) ID
        :type id: string
        :return: Get a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/groups/{group_id}/content_migrations/{id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_content_migration_users(request_ctx, user_id, id, **request_kwargs):
    """
    Returns data on an individual content migration

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param id: (required) ID
        :type id: string
        :return: Get a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/users/{user_id}/content_migrations/{id}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_content_migration_accounts(request_ctx, account_id, migration_type, pre_attachment_name, settings_file_url, pre_attachment[*]=None, settings_source_course_id=None, settings_folder_id=None, settings_overwrite_quizzes=None, settings_question_bank_id=None, settings_question_bank_name=None, date_shift_options_shift_dates=None, date_shift_options_old_start_date=None, date_shift_options_old_end_date=None, date_shift_options_new_start_date=None, date_shift_options_new_end_date=None, date_shift_options_day_substitutions=None, **request_kwargs):
    """
    Create a content migration. If the migration requires a file to be uploaded
    the actual processing of the file will start once the file upload process is completed.
    File uploading works as described in the {file:file_uploads.html File Upload Documentation}
    except that the values are set on a *pre_attachment* sub-hash.
    
    For migrations that don't require a file to be uploaded, like course copy, the
    processing will begin as soon as the migration is created.
    
    You can use the {api:ProgressController#show Progress API} to track the
    progress of the migration. The migration's progress is linked to with the
    _progress_url_ value.
    
    The two general workflows are:
    
    If no file upload is needed:
    
    1. POST to create
    2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
    
    For file uploading:
    
    1. POST to create with file info in *pre_attachment*
    2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
    3. {api:ContentMigrationsController#show GET} the ContentMigration
    4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
    
     (required if doing .zip file upload)

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param migration_type: (required) The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        :type migration_type: string
        :param pre_attachment_name: (required) Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        :type pre_attachment_name: string
        :param settings_file_url: (required) (optional) A URL to download the file from. Must not require authentication.
        :type settings_file_url: string
        :param pre_attachment[*]: (optional) Other file upload properties, See {file:file_uploads.html File Upload Documentation}
        :type pre_attachment[*]: string or None
        :param settings_source_course_id: (optional) The course to copy from for a course copy migration. (required if doing course copy)
        :type settings_source_course_id: string or None
        :param settings_folder_id: (optional) The folder to unzip the .zip file into for a zip_file_import.
        :type settings_folder_id: string or None
        :param settings_overwrite_quizzes: (optional) Whether to overwrite quizzes with the same identifiers between content packages.
        :type settings_overwrite_quizzes: boolean or None
        :param settings_question_bank_id: (optional) The existing question bank ID to import questions into if not specified in the content package.
        :type settings_question_bank_id: integer or None
        :param settings_question_bank_name: (optional) The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence.
        :type settings_question_bank_name: string or None
        :param date_shift_options_shift_dates: (optional) Whether to shift dates
        :type date_shift_options_shift_dates: boolean or None
        :param date_shift_options_old_start_date: (optional) The original start date of the source content/course
        :type date_shift_options_old_start_date: date or None
        :param date_shift_options_old_end_date: (optional) The original end date of the source content/course
        :type date_shift_options_old_end_date: date or None
        :param date_shift_options_new_start_date: (optional) The new start date for the content/course
        :type date_shift_options_new_start_date: date or None
        :param date_shift_options_new_end_date: (optional) The new end date for the source content/course
        :type date_shift_options_new_end_date: date or None
        :param date_shift_options_day_substitutions: (optional) Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        :type date_shift_options_day_substitutions: integer or None
        :return: Create a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/accounts/{account_id}/content_migrations'
    payload = {
        'migration_type' : migration_type,
        'pre_attachment[name]' : pre_attachment_name,
        'pre_attachment[*]' : pre_attachment[*],
        'settings[file_url]' : settings_file_url,
        'settings[source_course_id]' : settings_source_course_id,
        'settings[folder_id]' : settings_folder_id,
        'settings[overwrite_quizzes]' : settings_overwrite_quizzes,
        'settings[question_bank_id]' : settings_question_bank_id,
        'settings[question_bank_name]' : settings_question_bank_name,
        'date_shift_options[shift_dates]' : date_shift_options_shift_dates,
        'date_shift_options[old_start_date]' : date_shift_options_old_start_date,
        'date_shift_options[old_end_date]' : date_shift_options_old_end_date,
        'date_shift_options[new_start_date]' : date_shift_options_new_start_date,
        'date_shift_options[new_end_date]' : date_shift_options_new_end_date,
        'date_shift_options[day_substitutions][X]' : date_shift_options_day_substitutions,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_content_migration_courses(request_ctx, course_id, migration_type, pre_attachment_name, settings_file_url, pre_attachment[*]=None, settings_source_course_id=None, settings_folder_id=None, settings_overwrite_quizzes=None, settings_question_bank_id=None, settings_question_bank_name=None, date_shift_options_shift_dates=None, date_shift_options_old_start_date=None, date_shift_options_old_end_date=None, date_shift_options_new_start_date=None, date_shift_options_new_end_date=None, date_shift_options_day_substitutions=None, **request_kwargs):
    """
    Create a content migration. If the migration requires a file to be uploaded
    the actual processing of the file will start once the file upload process is completed.
    File uploading works as described in the {file:file_uploads.html File Upload Documentation}
    except that the values are set on a *pre_attachment* sub-hash.
    
    For migrations that don't require a file to be uploaded, like course copy, the
    processing will begin as soon as the migration is created.
    
    You can use the {api:ProgressController#show Progress API} to track the
    progress of the migration. The migration's progress is linked to with the
    _progress_url_ value.
    
    The two general workflows are:
    
    If no file upload is needed:
    
    1. POST to create
    2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
    
    For file uploading:
    
    1. POST to create with file info in *pre_attachment*
    2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
    3. {api:ContentMigrationsController#show GET} the ContentMigration
    4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
    
     (required if doing .zip file upload)

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param migration_type: (required) The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        :type migration_type: string
        :param pre_attachment_name: (required) Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        :type pre_attachment_name: string
        :param settings_file_url: (required) (optional) A URL to download the file from. Must not require authentication.
        :type settings_file_url: string
        :param pre_attachment[*]: (optional) Other file upload properties, See {file:file_uploads.html File Upload Documentation}
        :type pre_attachment[*]: string or None
        :param settings_source_course_id: (optional) The course to copy from for a course copy migration. (required if doing course copy)
        :type settings_source_course_id: string or None
        :param settings_folder_id: (optional) The folder to unzip the .zip file into for a zip_file_import.
        :type settings_folder_id: string or None
        :param settings_overwrite_quizzes: (optional) Whether to overwrite quizzes with the same identifiers between content packages.
        :type settings_overwrite_quizzes: boolean or None
        :param settings_question_bank_id: (optional) The existing question bank ID to import questions into if not specified in the content package.
        :type settings_question_bank_id: integer or None
        :param settings_question_bank_name: (optional) The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence.
        :type settings_question_bank_name: string or None
        :param date_shift_options_shift_dates: (optional) Whether to shift dates
        :type date_shift_options_shift_dates: boolean or None
        :param date_shift_options_old_start_date: (optional) The original start date of the source content/course
        :type date_shift_options_old_start_date: date or None
        :param date_shift_options_old_end_date: (optional) The original end date of the source content/course
        :type date_shift_options_old_end_date: date or None
        :param date_shift_options_new_start_date: (optional) The new start date for the content/course
        :type date_shift_options_new_start_date: date or None
        :param date_shift_options_new_end_date: (optional) The new end date for the source content/course
        :type date_shift_options_new_end_date: date or None
        :param date_shift_options_day_substitutions: (optional) Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        :type date_shift_options_day_substitutions: integer or None
        :return: Create a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/courses/{course_id}/content_migrations'
    payload = {
        'migration_type' : migration_type,
        'pre_attachment[name]' : pre_attachment_name,
        'pre_attachment[*]' : pre_attachment[*],
        'settings[file_url]' : settings_file_url,
        'settings[source_course_id]' : settings_source_course_id,
        'settings[folder_id]' : settings_folder_id,
        'settings[overwrite_quizzes]' : settings_overwrite_quizzes,
        'settings[question_bank_id]' : settings_question_bank_id,
        'settings[question_bank_name]' : settings_question_bank_name,
        'date_shift_options[shift_dates]' : date_shift_options_shift_dates,
        'date_shift_options[old_start_date]' : date_shift_options_old_start_date,
        'date_shift_options[old_end_date]' : date_shift_options_old_end_date,
        'date_shift_options[new_start_date]' : date_shift_options_new_start_date,
        'date_shift_options[new_end_date]' : date_shift_options_new_end_date,
        'date_shift_options[day_substitutions][X]' : date_shift_options_day_substitutions,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_content_migration_groups(request_ctx, group_id, migration_type, pre_attachment_name, settings_file_url, pre_attachment[*]=None, settings_source_course_id=None, settings_folder_id=None, settings_overwrite_quizzes=None, settings_question_bank_id=None, settings_question_bank_name=None, date_shift_options_shift_dates=None, date_shift_options_old_start_date=None, date_shift_options_old_end_date=None, date_shift_options_new_start_date=None, date_shift_options_new_end_date=None, date_shift_options_day_substitutions=None, **request_kwargs):
    """
    Create a content migration. If the migration requires a file to be uploaded
    the actual processing of the file will start once the file upload process is completed.
    File uploading works as described in the {file:file_uploads.html File Upload Documentation}
    except that the values are set on a *pre_attachment* sub-hash.
    
    For migrations that don't require a file to be uploaded, like course copy, the
    processing will begin as soon as the migration is created.
    
    You can use the {api:ProgressController#show Progress API} to track the
    progress of the migration. The migration's progress is linked to with the
    _progress_url_ value.
    
    The two general workflows are:
    
    If no file upload is needed:
    
    1. POST to create
    2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
    
    For file uploading:
    
    1. POST to create with file info in *pre_attachment*
    2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
    3. {api:ContentMigrationsController#show GET} the ContentMigration
    4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
    
     (required if doing .zip file upload)

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param migration_type: (required) The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        :type migration_type: string
        :param pre_attachment_name: (required) Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        :type pre_attachment_name: string
        :param settings_file_url: (required) (optional) A URL to download the file from. Must not require authentication.
        :type settings_file_url: string
        :param pre_attachment[*]: (optional) Other file upload properties, See {file:file_uploads.html File Upload Documentation}
        :type pre_attachment[*]: string or None
        :param settings_source_course_id: (optional) The course to copy from for a course copy migration. (required if doing course copy)
        :type settings_source_course_id: string or None
        :param settings_folder_id: (optional) The folder to unzip the .zip file into for a zip_file_import.
        :type settings_folder_id: string or None
        :param settings_overwrite_quizzes: (optional) Whether to overwrite quizzes with the same identifiers between content packages.
        :type settings_overwrite_quizzes: boolean or None
        :param settings_question_bank_id: (optional) The existing question bank ID to import questions into if not specified in the content package.
        :type settings_question_bank_id: integer or None
        :param settings_question_bank_name: (optional) The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence.
        :type settings_question_bank_name: string or None
        :param date_shift_options_shift_dates: (optional) Whether to shift dates
        :type date_shift_options_shift_dates: boolean or None
        :param date_shift_options_old_start_date: (optional) The original start date of the source content/course
        :type date_shift_options_old_start_date: date or None
        :param date_shift_options_old_end_date: (optional) The original end date of the source content/course
        :type date_shift_options_old_end_date: date or None
        :param date_shift_options_new_start_date: (optional) The new start date for the content/course
        :type date_shift_options_new_start_date: date or None
        :param date_shift_options_new_end_date: (optional) The new end date for the source content/course
        :type date_shift_options_new_end_date: date or None
        :param date_shift_options_day_substitutions: (optional) Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        :type date_shift_options_day_substitutions: integer or None
        :return: Create a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/groups/{group_id}/content_migrations'
    payload = {
        'migration_type' : migration_type,
        'pre_attachment[name]' : pre_attachment_name,
        'pre_attachment[*]' : pre_attachment[*],
        'settings[file_url]' : settings_file_url,
        'settings[source_course_id]' : settings_source_course_id,
        'settings[folder_id]' : settings_folder_id,
        'settings[overwrite_quizzes]' : settings_overwrite_quizzes,
        'settings[question_bank_id]' : settings_question_bank_id,
        'settings[question_bank_name]' : settings_question_bank_name,
        'date_shift_options[shift_dates]' : date_shift_options_shift_dates,
        'date_shift_options[old_start_date]' : date_shift_options_old_start_date,
        'date_shift_options[old_end_date]' : date_shift_options_old_end_date,
        'date_shift_options[new_start_date]' : date_shift_options_new_start_date,
        'date_shift_options[new_end_date]' : date_shift_options_new_end_date,
        'date_shift_options[day_substitutions][X]' : date_shift_options_day_substitutions,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_content_migration_users(request_ctx, user_id, migration_type, pre_attachment_name, settings_file_url, pre_attachment[*]=None, settings_source_course_id=None, settings_folder_id=None, settings_overwrite_quizzes=None, settings_question_bank_id=None, settings_question_bank_name=None, date_shift_options_shift_dates=None, date_shift_options_old_start_date=None, date_shift_options_old_end_date=None, date_shift_options_new_start_date=None, date_shift_options_new_end_date=None, date_shift_options_day_substitutions=None, **request_kwargs):
    """
    Create a content migration. If the migration requires a file to be uploaded
    the actual processing of the file will start once the file upload process is completed.
    File uploading works as described in the {file:file_uploads.html File Upload Documentation}
    except that the values are set on a *pre_attachment* sub-hash.
    
    For migrations that don't require a file to be uploaded, like course copy, the
    processing will begin as soon as the migration is created.
    
    You can use the {api:ProgressController#show Progress API} to track the
    progress of the migration. The migration's progress is linked to with the
    _progress_url_ value.
    
    The two general workflows are:
    
    If no file upload is needed:
    
    1. POST to create
    2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
    
    For file uploading:
    
    1. POST to create with file info in *pre_attachment*
    2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
    3. {api:ContentMigrationsController#show GET} the ContentMigration
    4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
    
     (required if doing .zip file upload)

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param migration_type: (required) The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        :type migration_type: string
        :param pre_attachment_name: (required) Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        :type pre_attachment_name: string
        :param settings_file_url: (required) (optional) A URL to download the file from. Must not require authentication.
        :type settings_file_url: string
        :param pre_attachment[*]: (optional) Other file upload properties, See {file:file_uploads.html File Upload Documentation}
        :type pre_attachment[*]: string or None
        :param settings_source_course_id: (optional) The course to copy from for a course copy migration. (required if doing course copy)
        :type settings_source_course_id: string or None
        :param settings_folder_id: (optional) The folder to unzip the .zip file into for a zip_file_import.
        :type settings_folder_id: string or None
        :param settings_overwrite_quizzes: (optional) Whether to overwrite quizzes with the same identifiers between content packages.
        :type settings_overwrite_quizzes: boolean or None
        :param settings_question_bank_id: (optional) The existing question bank ID to import questions into if not specified in the content package.
        :type settings_question_bank_id: integer or None
        :param settings_question_bank_name: (optional) The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence.
        :type settings_question_bank_name: string or None
        :param date_shift_options_shift_dates: (optional) Whether to shift dates
        :type date_shift_options_shift_dates: boolean or None
        :param date_shift_options_old_start_date: (optional) The original start date of the source content/course
        :type date_shift_options_old_start_date: date or None
        :param date_shift_options_old_end_date: (optional) The original end date of the source content/course
        :type date_shift_options_old_end_date: date or None
        :param date_shift_options_new_start_date: (optional) The new start date for the content/course
        :type date_shift_options_new_start_date: date or None
        :param date_shift_options_new_end_date: (optional) The new end date for the source content/course
        :type date_shift_options_new_end_date: date or None
        :param date_shift_options_day_substitutions: (optional) Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        :type date_shift_options_day_substitutions: integer or None
        :return: Create a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/users/{user_id}/content_migrations'
    payload = {
        'migration_type' : migration_type,
        'pre_attachment[name]' : pre_attachment_name,
        'pre_attachment[*]' : pre_attachment[*],
        'settings[file_url]' : settings_file_url,
        'settings[source_course_id]' : settings_source_course_id,
        'settings[folder_id]' : settings_folder_id,
        'settings[overwrite_quizzes]' : settings_overwrite_quizzes,
        'settings[question_bank_id]' : settings_question_bank_id,
        'settings[question_bank_name]' : settings_question_bank_name,
        'date_shift_options[shift_dates]' : date_shift_options_shift_dates,
        'date_shift_options[old_start_date]' : date_shift_options_old_start_date,
        'date_shift_options[old_end_date]' : date_shift_options_old_end_date,
        'date_shift_options[new_start_date]' : date_shift_options_new_start_date,
        'date_shift_options[new_end_date]' : date_shift_options_new_end_date,
        'date_shift_options[day_substitutions][X]' : date_shift_options_day_substitutions,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_content_migration_accounts(request_ctx, account_id, id, **request_kwargs):
    """
    Update a content migration. Takes same arguments as create except that you
    can't change the migration type. However, changing most settings after the
    migration process has started will not do anything. Generally updating the
    content migration will be used when there is a file upload problem. If the
    first upload has a problem you can supply new _pre_attachment_ values to
    start the process again.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Update a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/accounts/{account_id}/content_migrations/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def update_content_migration_courses(request_ctx, course_id, id, **request_kwargs):
    """
    Update a content migration. Takes same arguments as create except that you
    can't change the migration type. However, changing most settings after the
    migration process has started will not do anything. Generally updating the
    content migration will be used when there is a file upload problem. If the
    first upload has a problem you can supply new _pre_attachment_ values to
    start the process again.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Update a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/courses/{course_id}/content_migrations/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def update_content_migration_groups(request_ctx, group_id, id, **request_kwargs):
    """
    Update a content migration. Takes same arguments as create except that you
    can't change the migration type. However, changing most settings after the
    migration process has started will not do anything. Generally updating the
    content migration will be used when there is a file upload problem. If the
    first upload has a problem you can supply new _pre_attachment_ values to
    start the process again.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param id: (required) ID
        :type id: string
        :return: Update a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/groups/{group_id}/content_migrations/{id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, id=id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def update_content_migration_users(request_ctx, user_id, id, **request_kwargs):
    """
    Update a content migration. Takes same arguments as create except that you
    can't change the migration type. However, changing most settings after the
    migration process has started will not do anything. Generally updating the
    content migration will be used when there is a file upload problem. If the
    first upload has a problem you can supply new _pre_attachment_ values to
    start the process again.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param id: (required) ID
        :type id: string
        :return: Update a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/users/{user_id}/content_migrations/{id}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, id=id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def list_migration_systems_accounts(request_ctx, account_id, per_page=None, **request_kwargs):
    """
    Lists the currently available migration types. These values may change.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List Migration Systems
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/content_migrations/migrators'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_migration_systems_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Lists the currently available migration types. These values may change.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List Migration Systems
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/content_migrations/migrators'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_migration_systems_groups(request_ctx, group_id, per_page=None, **request_kwargs):
    """
    Lists the currently available migration types. These values may change.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List Migration Systems
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/groups/{group_id}/content_migrations/migrators'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_migration_systems_users(request_ctx, user_id, per_page=None, **request_kwargs):
    """
    Lists the currently available migration types. These values may change.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List Migration Systems
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/content_migrations/migrators'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


