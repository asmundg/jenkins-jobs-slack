# jenkins-jobs-slack

Slack publisher and config for jenkins job builder

# Getting started

    - project:
      name: foo
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

