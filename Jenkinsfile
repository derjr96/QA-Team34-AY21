pipeline {
	options {
    timestamps() // Append timestamps to each line
    timeout(time: 20, unit: 'MINUTES') // Set a timeout on the total execution time of the job
  	}
	agent any
	stages {
		stage('Checkout') { // Checkout (git clone ...) the projects repository
			steps {
				checkout scm
			}
		}
		stage('Build') {
			steps {
				echo "Building the docker image"
				sh "docker build -t django_image ."
			}
		}
		stage('OWASP DependencyCheck') {
			steps {
				dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Default'
			}
			post {
				success {
					dependencyCheckPublisher pattern: 'dependency-check-report.xml'
				}
			}
		}
        stage('Test') {
            agent {
                docker { image 'python:3'}
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python SecureWebApp/manage.py test SecureWebApp/website/tests -v 3'
                sh 'python SecureWebApp/manage.py test SecureWebApp/users/tests -v 3'
            }
        }
		stage('Linting') {
			agent {
				docker { image 'python:3' }
			} 
            steps {
                sh 'pip install flake8'
				sh 'flake8 --ignore W293,W292,W391,E501,E265,E303,E302,E126,E261,E251,E127,E128,E231,W605,W504 SecureWebApp'
            }
        }
		stage('Deploy')
			{
			steps {
				sh "docker stop django_image || true"
				echo "deploying the application"
				sh "docker run -d --rm -u root \
				-e VIRTUAL_HOST=3se2is.sitict.net \
				-e VIRTUAL_PORT=8000 \
				--name django_image \
				django_image"
			}
		}
	}
}