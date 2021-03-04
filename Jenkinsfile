pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') { 
            agent {
                docker {
                    // Build this image using the Dockerfile.base
                    image 'ubuntu_test_image:test'
                    args '-u 0'
                }
            }
            steps {
                sh "pip install -r requirements.txt"
                sh 'pyb run_unit_tests'
            }
        }
        // stage('Build') { 
        //     Add code to build and deploy this
        // }
    }

    
}