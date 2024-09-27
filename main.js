document.getElementById('sendMessageBtn').addEventListener('click', function() {
  // إرسال طلب إلى الخادم لتشغيل السكربت
  fetch('https://yourserver.com/send-message', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message: 'هذه رسالة من حسابي الشخصي!'
      }),
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        alert('تم إرسال الرسالة بنجاح!');
      } else {
        alert('حدث خطأ أثناء إرسال الرسالة.');
      }
    })
    .catch(error => {
      alert('حدث خطأ: ' + error);
    });
});