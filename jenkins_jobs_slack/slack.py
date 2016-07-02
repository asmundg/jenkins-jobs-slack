import xml.etree.ElementTree as XML

def slack_publisher(parser, xml_parent, data):
    """yaml: slack

    Example::

      publishers:
        - slack:
            team-domain: example.com
            auth-token: secret
            build-server-url: https://jenkins.example.com
            room: '#jenkins'
            notify-start: true
            notify-success: true
            notify-aborted: true
            notify-notbuilt: true
            notify-unstable: true
            notify-failure: true
            notify-backtonormal: true
            notify-repeatedfailure: true
            include-test-summary: true
            commit-info-choice: NONE | AUTHORS | AUTHORS_AND_TITLES
            include-custom-message: true
            custom-message: message

    """
    if data is None:
        data = dict()

    notifier = XML.SubElement(
        xml_parent, 'jenkins.plugins.slack.SlackNotifier')
    notifier.set('plugin', 'slack@2.0.1')

    for (opt, attr) in (('team-domain', 'teamDomain'),
                        ('auth-token', 'authToken'),
                        ('build-server-url', 'buildServerUrl'),
                        ('room', 'room'),
                        ('commit-info-choice', 'commitInfoChoice')):
        (XML.SubElement(notifier, attr).text) = data.get(opt)

    for (opt, attr) in (('notify-start', 'startNotification'),
                        ('notify-success', 'notifySuccess'),
                        ('notify-aborted', 'notifyAborted'),
                        ('notify-notbuilt', 'notifyNotBuilt'),
                        ('notify-unstable', 'notifyUnstable'),
                        ('notify-failure', 'notifyFailure'),
                        ('notify-backtonormal', 'notifyBackToNormal'),
                        ('notify-repeatedfailure', 'notifyRepeatedFailure'),
                        ('include-test-summary', 'includeTestSummary'),
                        ('include-custom-message', 'includeCustomMessage')):
        (XML.SubElement(notifier, attr)
         .text) = 'true' if data.get(opt, True) else 'false'

    if data.get('include-custom-message'):
        (XML.SubElement(notifier, 'customMessage')
         .text) = data.get('custom-message')