from canvas_sdk import client, utils


def list_roles(request_ctx, account_id, state=None, show_inherited=None, per_page=None, **request_kwargs):
    """
    List the roles available to an account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) The id of the account to retrieve roles for.
        :type account_id: string
        :param state: (optional) Filter by role state. If this argument is omitted, only 'active' roles are
returned.
        :type state: array or None
        :param show_inherited: (optional) If this argument is true, all roles inherited from parent accounts will
be included.
        :type show_inherited: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List roles
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    state_types = ('active', 'inactive')
    utils.validate_attr_is_acceptable(state, state_types)
    path = '/v1/accounts/{account_id}/roles'
    payload = {
        'state[]': state,
        'show_inherited': show_inherited,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_role(request_ctx, id, account_id, role_id, role=None, **request_kwargs):
    """
    Retrieve information about a single role

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param account_id: (required) The id of the account containing the role
        :type account_id: string
        :param role_id: (required) The unique identifier for the role
        :type role_id: integer
        :param role: (optional) The name for the role
        :type role: string or None
        :return: Get a single role
        :rtype: requests.Response (with Role data)

    """

    path = '/v1/accounts/{account_id}/roles/{id}'
    payload = {
        'role_id': role_id,
        'role': role,
    }
    url = request_ctx.base_api_url + path.format(id=id, account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_new_role(request_ctx, account_id, label, role=None, base_role_type=None, permissions_X_explicit=None, permissions_X_enabled=None, permissions_X_locked=None, permissions_X_applies_to_self=None, permissions_X_applies_to_descendants=None, **request_kwargs):
    """
    Create a new course-level or account-level role.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param label: (required) Label for the role.
        :type label: string
        :param role: (optional) Deprecated alias for label.
        :type role: string or None
        :param base_role_type: (optional) Specifies the role type that will be used as a base
for the permissions granted to this role.

Defaults to 'AccountMembership' if absent
        :type base_role_type: string or None
        :param permissions_X_explicit: (optional) no description
        :type permissions_X_explicit: boolean or None
        :param permissions_X_enabled: (optional) If explicit is 1 and enabled is 1, permission <X> will be explicitly
granted to this role. If explicit is 1 and enabled has any other value
(typically 0), permission <X> will be explicitly denied to this role. If
explicit is any other value (typically 0) or absent, or if enabled is
absent, the value for permission <X> will be inherited from upstream.
Ignored if permission <X> is locked upstream (in an ancestor account).

May occur multiple times with unique values for <X>. Recognized
permission names for <X> are:

  [For Account-Level Roles Only]
  become_user                      -- Become other users
  import_sis                       -- Import SIS data
  manage_account_memberships       -- Add/remove other admins for the account
  manage_account_settings          -- Manage account-level settings
  manage_alerts                    -- Manage global alerts
  manage_courses                   -- Manage ( add / edit / delete ) courses
  manage_developer_keys            -- Manage developer keys
  manage_global_outcomes           -- Manage learning outcomes
  manage_jobs                      -- Manage background jobs
  manage_role_overrides            -- Manage permissions
  manage_storage_quotas            -- Set storage quotas for courses, groups, and users
  manage_sis                       -- Manage SIS data
  manage_site_settings             -- Manage site-wide and plugin settings
  manage_user_logins               -- Modify login details for users
  read_course_content              -- View course content
  read_course_list                 -- View the list of courses
  read_messages                    -- View notifications sent to users
  site_admin                       -- Use the Site Admin section and admin all other accounts
  view_error_reports               -- View error reports
  view_statistics                  -- View statistics
  manage_feature_flags             -- Enable or disable features at an account level

  [For both Account-Level and Course-Level roles]
   Note: Applicable enrollment types for course-level roles are given in brackets:
         S = student, T = teacher, A = TA, D = designer, O = observer.
         Lower-case letters indicate permissions that are off by default.
         A missing letter indicates the permission cannot be enabled for the role
         or any derived custom roles.
  change_course_state              -- [ TaD ] Change course state
  comment_on_others_submissions    -- [sTAD ] View all students' submissions and make comments on them
  create_collaborations            -- [STADo] Create student collaborations
  create_conferences               -- [STADo] Create web conferences
  manage_admin_users               -- [ Tad ] Add/remove other teachers, course designers or TAs to the course
  manage_assignments               -- [ TADo] Manage (add / edit / delete) assignments and quizzes
  manage_calendar                  -- [sTADo] Add, edit and delete events on the course calendar
  manage_content                   -- [ TADo] Manage all other course content
  manage_files                     -- [ TADo] Manage (add / edit / delete) course files
  manage_grades                    -- [ TA  ] Edit grades
  manage_groups                    -- [ TAD ] Manage (create / edit / delete) groups
  manage_interaction_alerts        -- [ Ta  ] Manage alerts
  manage_outcomes                  -- [sTaDo] Manage learning outcomes
  manage_sections                  -- [ TaD ] Manage (create / edit / delete) course sections
  manage_students                  -- [ TAD ] Add/remove students for the course
  manage_user_notes                -- [ TA  ] Manage faculty journal entries
  manage_rubrics                   -- [ TAD ] Edit assessing rubrics
  manage_wiki                      -- [ TADo] Manage (add / edit / delete) pages
  read_forum                       -- [STADO] View discussions
  moderate_forum                   -- [sTADo] Moderate discussions (delete/edit others' posts, lock topics)
  post_to_forum                    -- [STADo] Post to discussions
  read_announcements               -- [STADO] View announcements
  read_question_banks              -- [ TADo] View and link to question banks
  read_reports                     -- [ TAD ] View usage reports for the course
  read_roster                      -- [STADo] See the list of users
  read_sis                         -- [sTa  ] Read SIS data
  send_messages                    -- [STADo] Send messages to individual course members
  send_messages_all                -- [sTADo] Send messages to the entire class
  view_all_grades                  -- [ TAd ] View all grades
  view_group_pages                 -- [sTADo] View the group pages of all student groups
  lti_add_edit                     -- [ TAD ] LTI add and edit

Some of these permissions are applicable only for roles on the site admin
account, on a root account, or for course-level roles with a particular base role type;
if a specified permission is inapplicable, it will be ignored.

Additional permissions may exist based on installed plugins.
        :type permissions_X_enabled: boolean or None
        :param permissions_X_locked: (optional) If the value is 1, permission <X> will be locked downstream (new roles in
subaccounts cannot override the setting). For any other value, permission
<X> is left unlocked. Ignored if permission <X> is already locked
upstream. May occur multiple times with unique values for <X>.
        :type permissions_X_locked: boolean or None
        :param permissions_X_applies_to_self: (optional) If the value is 1, permission <X> applies to the account this role is in.
The default value is 1. Must be true if applies_to_descendants is false.
This value is only returned if enabled is true.
        :type permissions_X_applies_to_self: boolean or None
        :param permissions_X_applies_to_descendants: (optional) If the value is 1, permission <X> cascades down to sub accounts of the
account this role is in. The default value is 1.  Must be true if
applies_to_self is false.This value is only returned if enabled is true.
        :type permissions_X_applies_to_descendants: boolean or None
        :return: Create a new role
        :rtype: requests.Response (with Role data)

    """

    base_role_type_types = ('AccountMembership', 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', 'DesignerEnrollment')
    utils.validate_attr_is_acceptable(base_role_type, base_role_type_types)
    path = '/v1/accounts/{account_id}/roles'
    payload = {
        'label': label,
        'role': role,
        'base_role_type': base_role_type,
        'permissions[X][explicit]': permissions_X_explicit,
        'permissions[X][enabled]': permissions_X_enabled,
        'permissions[X][locked]': permissions_X_locked,
        'permissions[X][applies_to_self]': permissions_X_applies_to_self,
        'permissions[X][applies_to_descendants]': permissions_X_applies_to_descendants,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def deactivate_role(request_ctx, account_id, id, role_id, role=None, **request_kwargs):
    """
    Deactivates a custom role.  This hides it in the user interface and prevents it
    from being assigned to new users.  Existing users assigned to the role will
    continue to function with the same permissions they had previously.
    Built-in roles cannot be deactivated.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param role_id: (required) The unique identifier for the role
        :type role_id: integer
        :param role: (optional) The name for the role
        :type role: string or None
        :return: Deactivate a role
        :rtype: requests.Response (with Role data)

    """

    path = '/v1/accounts/{account_id}/roles/{id}'
    payload = {
        'role_id': role_id,
        'role': role,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def activate_role(request_ctx, account_id, id, role_id, role=None, **request_kwargs):
    """
    Re-activates an inactive role (allowing it to be assigned to new users)

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param role_id: (required) The unique identifier for the role
        :type role_id: integer
        :param role: (optional) The name for the role
        :type role: Deprecated or None
        :return: Activate a role
        :rtype: requests.Response (with Role data)

    """

    path = '/v1/accounts/{account_id}/roles/{id}/activate'
    payload = {
        'role_id': role_id,
        'role': role,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_role(request_ctx, account_id, id, label=None, permissions_X_explicit=None, permissions_X_enabled=None, permissions_X_applies_to_self=None, permissions_X_applies_to_descendants=None, **request_kwargs):
    """
    Update permissions for an existing role.
    
    Recognized roles are:
    * TeacherEnrollment
    * StudentEnrollment
    * TaEnrollment
    * ObserverEnrollment
    * DesignerEnrollment
    * AccountAdmin
    * Any previously created custom role

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param label: (optional) The label for the role. Can only change the label of a custom role that belongs directly to the account.
        :type label: string or None
        :param permissions_X_explicit: (optional) no description
        :type permissions_X_explicit: boolean or None
        :param permissions_X_enabled: (optional) These arguments are described in the documentation for the
{api:RoleOverridesController#add_role add_role method}.
        :type permissions_X_enabled: boolean or None
        :param permissions_X_applies_to_self: (optional) If the value is 1, permission <X> applies to the account this role is in.
The default value is 1. Must be true if applies_to_descendants is false.
This value is only returned if enabled is true.
        :type permissions_X_applies_to_self: boolean or None
        :param permissions_X_applies_to_descendants: (optional) If the value is 1, permission <X> cascades down to sub accounts of the
account this role is in. The default value is 1.  Must be true if
applies_to_self is false.This value is only returned if enabled is true.
        :type permissions_X_applies_to_descendants: boolean or None
        :return: Update a role
        :rtype: requests.Response (with Role data)

    """

    path = '/v1/accounts/{account_id}/roles/{id}'
    payload = {
        'label': label,
        'permissions[X][explicit]': permissions_X_explicit,
        'permissions[X][enabled]': permissions_X_enabled,
        'permissions[X][applies_to_self]': permissions_X_applies_to_self,
        'permissions[X][applies_to_descendants]': permissions_X_applies_to_descendants,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


