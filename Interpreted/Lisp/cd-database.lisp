(defvar *db* nil)                      ; Database global variable

;;; Functions related to adding CDs
(defun make-cd (artist title rating ripped)
	(list :artist artist :title title :rating rating :ripped ripped))

(defun add-record (cd) (push cd *db*))

(defun prompt-read (prompt)
	(format *query-io* "~a: " prompt)
	(force-output *query-io*)
	(read-line *query-io*))

(defun prompt-for-cd ()
	(make-cd
		(prompt-read "Artist")
		(prompt-read "Title")
		(or (parse-integer (prompt-read "Rating") :junk-allowed t) 0)
		(yes-or-no (prompt-read "Ripped [y/n]: "))))
		
(defun add-cds ()
	(loop (add-record (prompt-for-cd))
		(if (equal (yes-or-no (prompt-read "Another [y/n]: ")) t) (return))))
		
(defun yes-or-no (input)
	(if (equal input "y") t)
	(if (equal input "n") nil))



;;; Printing and file related
(defun dump-db ()
	(dolist (cd *db*)
		(format t "~{~a:~10t~a~%~}~%" cd)))

(defun save-db (filename)
	(with-open-file (out filename
					 :direction :output
					 :if-exists :supersede)
		(with-standard-io-syntax
			(print *db* out))))

(defun load-db (filename)
	(with-open-file (in filename)
		(with-standard-io-syntax
			(setf *db* (read in)))))



;;; Selecting from db
(defun where (&key title artist rating (ripped nil ripped-p))
	;; cd record from remove-if-not iterator is passed here
	#'(lambda (cd)
		(and
			(if title 	 (equal (getf cd :title)  title)  t)
			(if artist 	 (equal (getf cd :artist) artist) t)
			(if rating 	 (equal (getf cd :rating) rating) t)
			(if ripped-p (equal (getf cd :ripped) ripped) t))))

(defun select (select-fn)
	(remove-if-not select-fn *db*))

(defun update (selector-fn &key artist title rating (ripped nil ripped-p))
	(setf *db*
		(mapcar
			#'(lambda (row)
				(when (funcall selector-fn row)
					(if artist   (setf (getf row :artist) artist))
					(if title    (setf (getf row :title)  title))
					(if rating   (setf (getf row :rating) rating))
					(if ripped-p (setf (getf row :ripped) ripped)))
				row) *db*)))

(defun delete-row (select-fn)
	(setf *db* (remove-if select-fn *db*)))
	
;;; Macro dark magic
(defun make-comparison-expr (field value)
	(list 'equal (list 'getf 'cd field) value))
