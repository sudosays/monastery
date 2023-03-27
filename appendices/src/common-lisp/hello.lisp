(defun main ()
  (print "hello, world"))

(defvar *cool* 123)

(setf *cool* nil)

(setf *cool* #'main)

