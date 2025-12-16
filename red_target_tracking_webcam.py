import cv2
import numpy as np

cap = cv2.VideoCapture(0)

print("🚁 DRONE CAMERA SIMULATION")
print("🎯 Track the red target")
print("❌ Press 'q' to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red color range in HSV (two ranges)
    lower_red_1 = np.array([0, 100, 100])
    upper_red_1 = np.array([10, 255, 255])

    lower_red_2 = np.array([170, 100, 100])
    upper_red_2 = np.array([180, 255, 255])

    # Create masks and combine them
    mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
    mask2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Find contours (target detection)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Select the largest contour
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)

        # Process only sufficiently large targets
        if area > 500:
            x, y, w, h = cv2.boundingRect(largest_contour)

            # Draw bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            # Calculate center point
            cx = x + w // 2
            cy = y + h // 2
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

            # Display target coordinates
            cv2.putText(
                frame,
                f"TARGET: ({cx}, {cy})",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Add HUD (Head-Up Display)
    cv2.rectangle(frame, (10, 10), (220, 80), (0, 0, 0), -1)
    cv2.putText(frame, "DRONE CAM", (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, "TRACKING MODE", (20, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

    # Display output
    cv2.imshow("🚁 Drone Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
