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
                sh "apt-get install git -y"
                sh "git clone 'https://github.com/Karthikeyan298/system-analyzer.git' && cd system-analyzer"
                sh 'pip3 install pybuilder' 
                sh 'pyb run_unit_tests'
            }
        }
        // stage('Build'){
        //     steps {
        //         sh 'make check'
        //         junit 'reports/**/*.xml' 
        //     }
        // }
        // stage('Deploy') {
        //     steps {
        //         sh 'make publish'
        //     }
        }

    
}