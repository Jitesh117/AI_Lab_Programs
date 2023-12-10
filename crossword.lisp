defparameter *crossword-grid* 
  '((#\- #\- #\- #\B #\Y #\T #\E)
    (#\- #\- #\- #\R #\- #\- #\-)
    (#\E #\N #\G #\I #\N #\E #\-)
    (#\- #\- #\- #\C #\- #\W #\D)
    (#\- #\G #\- #\K #\- #\I #\A)
    (#\C #\P #\U #\- #\- #\F #\T)
    (#\- #\U #\U #\S #\B #\I #\A)))
(defparameter *clues*




  '((:across 1 "It powers vehicles and machines with fuel or electricity.(6)" ENGINE)
    (:across 2 " The brain of the computer(3)" CPU)
    (:across 3 "Basic data storage unit(4)" BYTE)
    (:across 4 "The component which connects peripheral(3)" USB)
    (:down 5 "It's a rectangular building material made of clay or concrete, often used in construction.(5)" BRICK)
    (:down 6 "Raw form of Information(4)" DATA)
    (:down 7 "Graphical device which handles graphics(3)" GPU)
    (:down 8 "Connecting Wirelessly(4)" WIFI)))


(defun print-crossword-grid (grid)
  (format t "~%CROSSWORD PUZZLE: ~%" )
  (format t "(* indicate the cells where the words occur) ~%~%" )
  (loop for row in grid
    do (loop for cell in row
      do (if (char= cell #\-)
             (format t "~a " cell)
             (format t "* ")))
    do (format t "~%")))

(defun print-answer (grid)
    (loop for row in grid
    do (loop for cell in row
             do (format t "~a " cell))
    do (format t "~%")))

(defun check-answer (user-input answer)
      (if (string= user-input answer)
      (format t "RIGHT!~%")
      (progn
        (format t "WRONG. Try again.~%")
        (loop
          (format t "Enter your answer again: ")
          (finish-output)
          (let ((user-input (read-line *query-io*)))
            (if (string= user-input answer)



                (progn
                  (format t "RIGHT!~%")
                  (return)) ; Exit the loop if the answer is correct
                (format t "WRONG. Try again.~%")))))))


(defun play-crossword (clues)
  (format t "Welcome to the crossword puzzle!~%")
  (format t "Let's get started.~%")
  (print-crossword-grid *crossword-grid*)
  (format t "~%CLUES:~%~%")
  (loop for clue in clues
    do (format t "Direction: [~a] ~a~%" (car clue) (caddr clue))
    do (format t "Enter your answer: ")
    do (finish-output)
    do (let ((user-input (read-line *query-io*)))
          (check-answer user-input (cadddr clue))))
  (format t "Congratulations, you've completed the puzzle!~%")
  (print-answer *crossword-grid*)
)

(play-crossword *clues*)
