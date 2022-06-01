-- Акция подписка light для всех кто просто привяжет карту
UPDATE clients
INNER JOIN cards ON clients.id = cards.owner
SET clients.subscription_id = '2'
WHERE cards.`number` IS NOT NULL
AND clients.subscription_id = '1';


PREPARE change_subscription FROM
'UPDATE clients
SET clients.subscription_id = '3'
WHERE clients.id = ?';

SET @clients_id = '2';
EXECUTE change_subscription USING @clients_id;