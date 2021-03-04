pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') { 
            agent {
                docker {
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
        //     agent {
        //         docker {
        //             image 'ubuntu_test_image:test'
        //             args '-u 0'
        //         }
        //     }
        //     steps {
        //         sh "cd system-analyzer"
        //         sh 'pip install pybuilder' 
        //         sh 'pyb run_unit_tests'
        //     }
        // }
    }

    
}