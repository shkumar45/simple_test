/* groovylint-disable-next-line CompileStatic */
pipeline {
    agent any

    // def importTestResultsToJira(){

    // }

    stages {
        stage('Checkout') {
            steps {
                // Pull code from the Git repository
                git url: 'https://github.com/shkumar45/simple_test.git', branch: 'main'
            }
        }

        stage('Set Up Python') {
            steps {
                // Install Python dependencies
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run Python unit tests
                sh 'source venv/bin/activate && python -m unittest discover'
                // importTestResultsToJira()
                script{
                    req_payload = '{ "testExecutionKey": "XRAYT-5",\
                            "info" : {\
                                "summary" : "Execution of automated tests for release v1.3",\
                                "description" : "test execution",\
                                "user" : "admin",\
                                "revision" : "1.0.42134",\
                                "startDate" : "2014-08-30T11:47:35+01:00",\
                                "finishDate" : "2014-08-30T11:53:00+01:00",\
                                "testPlanKey" : "XRAYT-1",\
                                "testEnvironments": ["local"]\
                            },\
                            "tests" : [\
                                {\
                                    "testKey" : "XRAYT-2",\
                                    "start" : "2024-08-30T11:47:35+01:00",\
                                    "finish" : "2024-08-30T11:50:56+01:00",\
                                    "comment" : "Successful execution",\
                                    "status" : "PASS"\
                                }\
                            ]\
                        }'
                    JIRA_TOKEN = credentials('JIRA_TOKEN')
                    response = httpRequest(
                        httpMode: 'POST',
                        url: 'http://localhost:8080/rest/raven/2.0/api/import/execution',
                        acceptType: 'APPLICATION_JSON',
                        contentType: 'APPLICATION_FORM_DATA',
                        requestBody: req_payload,
                        customHeaders: [[maskValue: false, name: 'Authorization', value: "Bearer ${JIRA_TOKEN}"]]
                    )
                    echo "Status: ${response.status}"
                    echo "Response: ${response.content}"
                }
            }
        }
    }

    post {
        always {
            // Clean workspace after build
            cleanWs()
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
